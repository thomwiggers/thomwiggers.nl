---
layout: post
category: crypto
title: Server hardening guide
date: 2016-01-16 22:13:09
---

I operate a couple of servers and I like to harden them to reduce the attack
surface. Since most of my systems are pretty up-to-date, I do not need the
default "compatible with everything" configurations.

## Securing HTTPS

### Use Letsencrypt

### Generate Diffie-Hellman parameters

Blablabla [Logjam][logjam].

    openssl dhparam 2048 > /etc/ssl/dhparam.pem

Why not 4096 bits? You can use it, but I don't expect 2048 bits to be broken any
time soon, and after quantum computers start showing up 4096 bits won't really
be much better than 2048 bits.

### Setting up your webserver

https://mozilla.github.io/server-side-tls/ssl-config-generator/

Watch out for Letsencrypt deploying their own shit.


## Securing OpenSSH

You can set up SSH to prefer Elliptic Curve cryptography over RSA, and use
modern key exchange algorithms without exposing yourself to
[Logjam][logjam]-style attacks. Finally, it's also good to get rid of SHA1 and
MD5.

A good resource is
[the OpenSSH Guidelines page on the Mozillawiki][mozopenssh].
You can basically copy the config.

Caveat: I found out that the version of paramiko in Debian Jessie does not
support SHA2 hashes or ECC in the key exchange. If you upgrade to the most
recent version from `pypi` you can use `diffie-hellman-exchange-group-sha256`.

[mozopenssh]: https://wiki.mozilla.org/Security/Guidelines/OpenSSH
[logjam]: https://weakdh.org
[moztls]: https://wiki.mozilla.org/Security/Server_Side_TLS
