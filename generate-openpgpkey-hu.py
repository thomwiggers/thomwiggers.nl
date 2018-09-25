#!/usr/bin/python3
#
# generate-openpgpkey-hu-3
# Copyright 2017, W. Martin Borgert <debacle@debian.org>
# License: GPL-3+
#
# This script has the same purpose as generate-openpgpkey-hu by Thomas
# Arendsen Hein and Andre Heinecke of Intevation GmbH, but:
#  - is Python 3 instead of Python 2
#  - uses python-gnupg instead of python-pyme (removed from Debian)
#  - is licensed GPL-3+ (like GnuPG) or later instead of GPL-2+
#  - uses encode_zbase32 function by Tocho Tochev
#  - is PEP8 clean :~)

import argparse
import email.utils
import functools
import hashlib
import itertools
import logging
import os
import sys

try:
    import gnupg
except ImportError:
    gnupg = None


def getargs():
    ap = argparse.ArgumentParser(
        description='generate contents of https://.../.well-known/openpgpkey/'
        + 'hu/ for OpenPGP Web Key Directory (WKD) from GnuPG keyring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('-a', '--address', action='append',
                    help='specific email address, more than one possible')
    ap.add_argument('-d', '--debug', action='store_true',
                    help='print debug output')
    ap.add_argument('-e', '--exist-ok', action='store_true',
                    help='accept, if target directory already exists')
    ap.add_argument('-k', '--keyring',
                    help='keyring to parse (or use default GnuPG keyring)')
    ap.add_argument('-m', '--mail-domain',
                    help='mail domain to filter keys')
    ap.add_argument('-o', '--output-dir', default="hu",
                    help='directory to write keys')
    ap.add_argument('-x', '--include-expired', action='store_true',
                    help='include expired keys')
    return ap.parse_args()


# Source: https://gist.githubusercontent.com/tochev/99f19d9ce062f1c7e203
# /raw/0077ec38adc350e0fd1207e6a525de482b40df7e/zbase32.py
# Copyright: Tocho Tochev <tocho AT tochev DOT net>
# Licence: MIT
# See http://philzimmermann.com/docs/human-oriented-base-32-encoding.txt
def encode_zbase32(bs):
    """
    Encode bytes bs using zbase32 encoding.
    Returns: bytearray

    >>> encode_zbase32(b'\\xd4z\\x04') == b'4t7ye'
    True
    """
    ALPTHABET = b"ybndrfg8ejkmcpqxot1uwisza345h769"
    result = bytearray()
    for word in itertools.zip_longest(*([iter(bs)] * 5)):
        padding_count = word.count(None)
        n = functools.reduce(lambda x, y: (x << 8) + (y or 0), word, 0)
        for i in range(0, (40 - 8 * padding_count), 5):
            result.append(ALPTHABET[(n >> (35 - i)) & 0x1F])
    return result


def localpart2zbase32(s):
    """transforms local part to lower case, SHA1s it, and encodes zbase32

    See https://tools.ietf.org/id/draft-koch-openpgp-webkey-service-01.html

    >>> localpart2zbase32('Joe.Doe')
    'iy9q119eutrkn8s1mk4r39qejnbu3n5q'
    """
    return encode_zbase32(
        hashlib.sha1(s.lower().encode("utf-8")).digest()).decode("utf-8")


class HU:
    def __init__(self, debug, keyring, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=args.exist_ok)
        except FileExistsError:
            print("Output directory " + output_dir
                  + " already exists, exiting!", file=sys.stderr)
            sys.exit(1)

        if debug:
            gnupg.logger.setLevel(logging.DEBUG)
            gnupg.logger.addHandler(logging.StreamHandler())

        self.debug = debug
        self.gpg = gnupg.GPG(keyring=keyring)
        self.output_dir = output_dir

    def get_fps(self, mail_domain, include_expired, addresses):
        """return dict of localpart: fingerprint"""
        fps = {}

        for key in self.gpg.list_keys():
            for uid in key.get('uids', []):
                addr = email.utils.parseaddr(uid)[1]
                if '@' not in addr:
                    continue
                local, domain = addr.split("@", 1)
                # trust: 'd' = disabled, 'e' = expired, 'r' = revoked
                if mail_domain and domain.lower() != mail_domain.lower() \
                        or key['trust'] in ['d', 'r'] \
                        or not include_expired and key['trust'] == 'e' \
                        or addresses and addr not in addresses:
                    continue
                if local in fps and fps[local] != key['fingerprint']:
                    print("Multiple options for %s! None used." % local,
                          file=sys.stderr)
                    del fps[local]
                else:
                    fps[local] = key['fingerprint']

        return fps

    def write_keys(self, fps):
        for local, fingerprint in fps.items():
            with open(os.path.join(self.output_dir,
                                   localpart2zbase32(local)), "wb") as f:
                f.write(self.gpg.export_keys(fingerprint, armor=False))
        print("Wrote %d keys to directory '%s'" % (len(fps), self.output_dir))


if __name__ == "__main__":
    args = getargs()

    if gnupg is None:
        print("Please 'apt install python3-gnupg'!", file=sys.stderr)
        sys.exit(1)

    hu = HU(args.debug, args.keyring, args.output_dir)
    fps = hu.get_fps(args.mail_domain, args.include_expired, args.address)
    hu.write_keys(fps)

