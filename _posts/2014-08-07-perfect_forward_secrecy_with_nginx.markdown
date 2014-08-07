---
layout: post
category: linux
title: Perfect forward secrecy with nginx
date: 2014-08-07 19:30:02
tags:
  - linux
  - nginx
  - ssl
  - https
  - server
---

Today, I enabled perfect forward secrecy on my `nginx` installation. I'm writing
down the config so I can easily find it later.

<!-- more -->

I just put the below config lines in a file called
`/etc/nginx/conf.d/ssl.conf` and now [SSLlabs][1] show PFS is enabled.

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers EECDH+ECDSA+AESGCM:EECDH+aRSA+AESGCM:EECDH+ECDSA+SHA256:EECDH+aRSA+RC4:EDH+aRSA:EECDH:RC4:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS;

Don't forget to restart nginx after making this change.
