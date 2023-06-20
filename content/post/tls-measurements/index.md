---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Post-quantum TLS experiments"
subtitle: "Instantiations, transmission requirements, and performance measurements for NIST security levels I, III and V"
summary: ""
authors: ["thom"]
tags: ["tls", "research", "post-quantum cryptography"]
categories: ["research"]
date: 2023-06-20T15:03:27+02:00
lastmod: 2023-06-20T15:03:27+02:00
featured: true
draft: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Scatter plot of the TLS experiments' handshake latency and size"
  focal_point: "TopLeft"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
Recently, I have computed the sizes and measured the performance of post-quantum TLS (both PQ key exchange and post-quantum authentication). In these experiments, I have examined combinations of Kyber, Dilithium, Falcon, SPHINCS<sup>+</sup>-(sf), HQC and (custom versions of) XMSS<sup>MT</sup>. The experiments include measuring their performance over two network settings, one high-bandwidth, low-latency and one low-bandwidth, high-latency connection.
I have examined the instances at NIST PQC security levels I, III and V, and for both unilaterally authenticated and mutually authenticated TLS.

The report on these experiments (which is basically an excerpt of my PhD thesis manuscript) can be found in the attached document. It's a fairly dense document, so refer to the reading suggestions to easily find what you are looking for.
I hope this document can be useful to get a feeling for how we can combine (signature) algorithms to fit their differing roles in the handshake, to see how this affects the handshake sizes, and have some indication of how the performance of these combinations of algorithms is in a TLS stack on a network. Additionally, I believe my results are useful to compare the cost of different NIST security levels.

The experiments do not include `SCT`s or `OSCP` staples, but I think that their effect can mostly be extrapolated from the reported results. Also note that I am simulating the network environment, so the effect of the initial congestion window is much less gradual than observed in practice.
As I write in the document, I want to examine the NIST on-ramp candidates' suitability for use in TLS as soon as the list of algorithms is formally out; for my PhD thesis they unfortunately came into the picture too late.

[Find the document here](handout-tls.pdf)