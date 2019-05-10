---
layout: post
category: security
title: Securing OpenSSH
date: 2016-01-29 16:27:03 +0100
authors: ["thom"]
---

You can set up SSH to prefer Elliptic Curve cryptography over RSA, and use
modern key exchange algorithms without exposing yourself to
[Logjam][logjam]-style attacks. It's also good to get rid of SHA1 and MD5.

A good resource is
[the OpenSSH Guidelines page on the Mozilla wiki][mozopenssh].
You can basically copy the config.

Caveat: I found out that the version of Paramiko in Debian Jessie does not
support SHA2 hashes or ECC in the key exchange. Paramiko was used in my case
by duplicity. If you upgrade to the most recent version from `pypi` you can
use `diffie-hellman-exchange-group-sha256`.

[mozopenssh]: https://wiki.mozilla.org/Security/Guidelines/OpenSSH
[logjam]: https://weakdh.org
