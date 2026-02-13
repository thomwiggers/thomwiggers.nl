---
layout: post
title: Certificate signing with an ePass2003
tags:
  - openssl
  - certificates
  - ssl
  - ca
  - epass2003
  - pki
categories:
  - security
authors: ["me"]
author_url: http://thomwiggers.nl/about.html

date: 2014-06-10
lastmod: 2015-01-22
highlight: true

---

I have a fairly creative ssl setup on my webserver:

* I run my own 'certificate authority' which signs the server certificate;
* I have a bunch of alternative names specified;
* The CA certificate sits on an ePass 2003 PKI token.

I'm writing down how I sign certificates in this context so I can use this to
look up the procedure instead of spending hours in DuckDuckGo. This is more of
a tutorial than elegant prose.

<!--more-->

Creating the certificate request:
---------------------------------

I use this openssl config, saved as `req.cnf`. I found an example version file
somewhere but I can't remember where, this is the one with my own modifications.

```plain
[ req ]
default_bits = 4096
default_keyfile = server.rded.nl.key
encrypt_key = no
default_md = sha256
prompt = no
utf8 = yes
req_extensions = my_extensions
distinguished_name = my_req_name

[ my_req_name ]
C = NL
ST = Gelderland
L = Nijmegen
O = Thom Wiggers servers
CN = *.rded.nl

[ my_extensions ]
basicConstraints=CA:FALSE
subjectAltName=@my_subject_alts
subjectKeyIdentifier = hash

[my_subject_alts]
DNS.1 = *.thomwiggers.nl
DNS.2 = thomwiggers.nl
DNS.3 = *.rded.nl
DNS.4 = rded.nl
DNS.5 = *.clearlyreta.rded.nl
```

I use this command to then create a new certificate request:

```sh
openssl req -new -key /etc/ssl/private/wildcard_private.key \
   -out server.csr -config req.cnf -days 365
```

File `wildcard_private.key` is my private key. You might still need to generate
one.

Sign the certificate request:
---------

Step 1: figure out the key id:

```sh
$ pkcs15-tool --list-keys
```
(Thom, it's the one with `a16`)


Then start the openssl console and execute the following (be sure to replace
`<id>`):

```sh
$ openssl
OpenSSL> engine dynamic \
  -pre SO_PATH:/usr/lib/engines/engine_pkcs11.so \
  -pre ID:pkcs11 \
  -pre LIST_ADD:1 \
  -pre LOAD \
  -pre MODULE_PATH:opensc-pkcs11.so

OpenSSL> ca -engine pkcs11 \
   -keyform engine \
   -cert ca.pem \
   -keyfile slot_1-id_<id> \
   -in wildcard_2_request.csr \
   -out cert.pem \
   -outdir . \
   -days 365
```

And then you can upload `cert.pem` back to your server.

Weird stuff:
------------

* I had to run the signing step as root and had to add some weird files in
  `/etc/ssl/`.

* You get a non-obvious error if you issue a new cert for other domains with
  the same subject.

Sources:
--------

* [Gooze tutorial](http://www.gooze.eu/howto/smartcard-quickstarter-guide/scenario-3-creating-a-self-signed-certificate-using-embedded)
* [OpenSC wiki](https://github.com/OpenSC/OpenSC/wiki/Engine-pkcs11-quickstart)
* `man` pages of `openssl`

Edits:
------

**2015-1-22:** Updated `req.cnf` to have better defaults, added same-subject note.
