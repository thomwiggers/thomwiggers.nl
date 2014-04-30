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
<p>Instead of trusting Telegram (which is a bad idea, try using Google for a few minutes, or <a href="http://unhandledexpression.com/2013/12/17/telegram-stand-back-we-know-maths/">start</a> <a href="http://www.thoughtcrime.org/blog/telegram-crypto-challenge/">here</a>) I'm going to bet on TextSecure, which actually does something which resembles OTR.</p>

<p>If you wish to verify it, my TextSecure identity is this:</p>
<p><a href="/files/textsecure-identity.png"><img alt="Textsecure identity QR code" src="/files/textsecure-identity.png" width="708" height="707" /></a></p>
<p>You can verify it's me by <a href="/files/textsecure-identity.png.asc">the image's PGP signature available here</a>, if there exists a trust path between us.</p>

```
~$ gpg --verify textsecure-identity.png.asc
gpg: Signature made Tue 25 Feb 2014 02:34:36 CET using RSA key ID 4871E82F
gpg: Good signature from "Thom Wiggers <thom@thomwiggers.nl>"
gpg:                 aka "Thom Wiggers (Alternate address) <thom@rded.nl>"
gpg:                 aka "[jpeg image of size 5009]"
```
