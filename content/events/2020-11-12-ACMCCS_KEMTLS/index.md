---
title: Post-Quantum TLS without handshake signatures
event_url: https://www.sigsac.org/ccs/CCS2020/
location: Virtual
address:
  street: null
  city: null
  region: null
  postcode: null
  country: null
summary: Conference talk about Post-Quantum TLS without Handshake Signatures at ACM CCS (virtual).
abstract: |
  It's possible to make TLS 1.3 post-quantum secure by just plugging in post-quantum key exchange and a post-quantum signature scheme. But PQ signatures tend to be quite big and slow. KEMTLS is our proposal for a post-quantum secure variant of TLS that authenticates by using KEMs instead of the handshake signature. With a trick to preserve the ability to allow the client to send the request after the server sends its certificate: using KEMs instead of signatures doesn't take more round trips for this first message.
  We compare a few instantiations of KEMTLS. Optimised for communication size, KEMTLS, with SIKE for KEX and handshake authentication, GeMSS for the CA certificate and a custom XMSS for optional intermediate certificates, requires less than half the bandwidth of a post-quantum TLS 1.3 using Falcon for the handshake signature. When picking primitives for speed, KEMTLS reduces the amount of server CPU cycles by up to 90% compared to an equivalent post-quantum instantiation of TLS 1.3, as well as reducing the time before the client can send its first application data.
date: 2021-01-11
authors:
  - me
tags:
  - KEMTLS
  - PQTLS
  - Post-Quantum
  - research
featured: false
image:
  caption: ""
  focal_point: ""
  preview_only: false
links:
  - type: slides
    url: presentation.pdf
  - type: pdf
    url: https://dl.acm.org/doi/10.1145/3372297.3423350
  - type: video
    url: https://dl.acm.org/doi/10.1145/3372297.3423350
slides: ""
projects:
  - kemtls
event_start: 2020-11-09
event_end: 2020-11-13
event_all_day: true
event_name: ACM CCS
---
