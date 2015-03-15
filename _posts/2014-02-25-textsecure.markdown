---
layout: post
status: publish
published: true
title: TextSecure
author: Thom Wiggers
author_login: Thom Wiggers
author_url: http://thomwiggers.nl
date: '2014-02-25 01:51:46 +0100'
date_gmt: '2014-02-25 00:51:46 +0100'
categories:
- security
tags:
- security
- gpg
- crypto
- pgp
- textsecure
- telegram

---

<p>Instead of trusting Telegram (which is a bad idea, try using Google for a few
minutes, or <a
href="http://unhandledexpression.com/2013/12/17/telegram-stand-back-we-know-maths/">start</a>
<a href="http://www.thoughtcrime.org/blog/telegram-crypto-challenge/">here</a>)
I'm going to bet on TextSecure, which actually does something other
cryptographers agree with..</p>

<!-- more -->

<p>If you wish to verify it, my TextSecure identity is this:</p>
<p><a href="/files/textsecure-identity.png"><img alt="Textsecure identity QR code" src="/files/textsecure-identity.png" width="708" height="707" /></a></p>
<p>You can verify it's me by <a href="/files/textsecure-identity.png.asc">the image's PGP signature available here</a>, if there exists a trust path between us.</p>

```
$ gpg --verify textsecure-identity.png.asc
gpg: assuming signed data in 'textsecure-identity.png'
gpg: Signature made Sun 15 Mar 2015 23:59:12 CET
gpg:                using DSA key 0x4175F59CF3EB45FC
gpg: Good signature from "Thom Wiggers <thom@thomwiggers.nl>" [ultimate]
gpg:                 aka "Thom Wiggers (Alternate address) <thom@rded.nl>" [ultimate]
gpg:                 aka "Thom Wiggers (Radboud University email) <t.wiggers@ru.nl>" [ultimate]
gpg:                 aka "[jpeg image of size 5009]" [ultimate]
Primary key fingerprint: C313 856D 66DA 0DDD DC5C  6203 915D 4ED3 4871 E82F
     Subkey fingerprint: 7082 D299 60EA D3F1 5F21  C85F 4175 F59C F3EB 45FC
```

**Edit 2015-03-16:** Updated image to match my new key on my new phone.
