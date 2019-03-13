---
layout: post
status: publish
published: true
title: OpenSC, Gentoo & Feitian ePass 2003
authors: ["thom"]
author_login: Thom Wiggers
author_url: http://thomwiggers.nl
date: '2013-05-25 22:29:55 +0200'
date_gmt: '2013-05-25 21:29:55 +0200'
categories:
- Linux
tags:
- linux
- pki
- epass2003
- gentoo
- english
comments: []
---

<p>While playing with my ePass2003 on my Gentoo installation today, I had some
trouble getting it to work. As it turned out, you need the following use flags
enabled:</p>

```
# /etc/portage/package.use
dev-libs/opensc pcsc-lite secure-messaging
```

<p>Hope this helps someone.</p>
