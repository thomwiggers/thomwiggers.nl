---
layout: post
category: code
title: Bitcoin private key qrcode scraper
date: 2015-11-01 21:28:36
authors: ["thom"]
---
[Tegenlicht][0] today had an [episode about Bitcoin][1] where they announced
they were going to give away €100 in Bitcoin. They were going to put up
a Bitcoin wallet private key as a QR-code on the screen.

It seemed to me like a fun project to try and grab that Bitcoin. I coded an
app that takes a screenshot every couple seconds and then tries to detect
all QR-codes in it. If any of the codes look like a private key, I then used
the [Blockcypher][2] API to determine the balance and empty the account into
my own wallet.

Unfortunately, the NPO stream was probably too slow and I was a couple moments
too late. It still was a fun challenge to program though and I learnt a bit
about how Bitcoin works.

[The code is available on here on Github][3]

[0]: http://tegenlicht.vpro.nl
[1]: http://tegenlicht.vpro.nl/afleveringen/2015-2016/bitcoin-evangelie.html
[2]: https://blockcypher.com
[3]: https://github.com/thomwiggers/screenscraper
