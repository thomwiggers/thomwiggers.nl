---
layout: post
category: linux
title: Perfect forward secrecy and HSTS with nginx
date: 2014-08-07 19:30:02
lastmod: 2014-08-07 19:30:02
tags:
  - linux
  - nginx
  - ssl
  - https
  - server
  - ocsp
  - ocsp stapling
authors:
  - me
---

Today, I enabled perfect forward secrecy on my `nginx` installation. I'm writing
down the config so I can easily find it later.

<!--more-->

I just put the below config lines in a file called
`/etc/nginx/conf.d/ssl.conf` and now [SSLlabs][1] show PFS is enabled.

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK;
    ssl_session_cache builtin:1000 shared:SSL:10m;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;


The SSL cipher suite has been borrowed from [this Mozilla wiki][2].

You need to create `dhparam.pem` by doing this in a root shell:

    # openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096

Enable HTTP Strict Transport Security (HSTS) by putting this in the relevant site configs:

    add_header Strict-Transport-Security max-age=63072000;

To add OSCP stapling, also add these lines:

    ssl_trusted_certificate /path/to/intermediates/plus/ca/root/certificate;
    ssl_stapling on;
    ssl_stapling_verify on;

To prevent attacks with `<iframe>` tags, add:

    add_header X-Frame-Options DENY; # or SAMEORIGIN

To stop browsers from sniffing the MIME response type:

    add_header X-Content-Type-Options nosniff;

Don't forget to restart nginx after making this change.

  [1]: https://www.ssllabs.com/ssltest/
  [2]: https://wiki.mozilla.org/Security/Server_Side_TLS
