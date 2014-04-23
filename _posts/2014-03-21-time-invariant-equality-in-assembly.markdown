---
layout: post
status: publish
published: true
title: Time-invariant equality in assembly
author: Thom Wiggers
author_login: Thom Wiggers
author_email: thom@thomwiggers.nl
author_url: http://thomwiggers.nl
wordpress_id: 71
wordpress_url: http://thomwiggers.nl/?p=71
date: '2014-03-21 18:25:10 +0100'
date_gmt: '2014-03-21 17:25:10 +0100'
categories:
- security
tags: [assembly crypto]
comments: []
---
<p>For crypto code it's important that it's time-invariant, otherwise it is vulnerable to timing attacks. I've had to build this time-invariant equality test from scratch, because I couldn't find something on Google. I hope it's useful to someone else. </p>
{% gist 9690984 %}
