---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "KEMTLS vs. Post-Quantum TLS: Performance on Embedded Systems"
authors: ['Ruben Gonzalez', 'thom']
date: 2022-12-06T12:01:41+01:00
doi: "10.1007/978-3-031-22829-2_6"

# Schedule page publish date (NOT publication's date).
publishDate: 2022-12-06T12:01:41+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "SPACE 2022: International Conference on Security, Privacy and Applied Cryptographic Engineering"
publication_short: "SPACE 2022"

abstract: |
  TLS is ubiquitous in modern computer networks.
  It secures transport for high-end desktops and low-end embedded devices alike.
  However, the public key cryptosystems currently used within TLS may soon be obsolete as large-scale quantum computers, once realized, would be able to break them.
  This threat has led to the development of post-quantum cryptography (PQC).
  The U.S. standardization body NIST is currently in the process of concluding a multi-year search for promising post-quantum signature schemes and key encapsulation mechanisms (KEMs).
  With the first PQC standards around the corner, TLS will have to be updated soon.
  However, especially for small microcontrollers, it appears the current NIST post-quantum signature finalists pose a challenge.
  Dilithium suffers from very large public keys and signatures; while Falcon has significant hardware requirements for efficient implementations.

  KEMTLS is a proposal for an alternative TLS handshake protocol that avoids authentication through signatures in the TLS handshake.
  Instead, it authenticates the peers through long-term KEM keys held in the certificates.
  The KEMs considered for standardization are more efficient in terms of computation and/or bandwidth than the post-quantum signature schemes.

  In this work, we compare KEMTLS to TLS 1.3 in an embedded setting.
  To gain meaningful results, we present implementations of KEMTLS and TLS 1.3 on a Cortex-M4-based platform.
  These implementations are based on the popular WolfSSL embedded TLS library and hence share a majority of their code.
  In our experiments, we consider both protocols with the remaining NIST finalist signature schemes and KEMs, except for Classic McEliece which has too large public keys.
  Both protocols are benchmarked and compared in terms of run-time, memory usage, traffic volume and code size.
  The benchmarks are performed in network settings relevant to the Internet of Things, namely low-latency broadband, LTE-M and Narrowband IoT.
  Our results show that KEMTLS can reduce handshake time by up to 38%, can lower peak memory consumption and can save traffic volume compared to TLS 1.3.

# Summary. An optional shortened abstract.
summary: "We investigate the performance of KEMTLS and PQ instantiations of TLS 1.3 on embedded devices."

tags: ['kemtls', 'research']
categories: ['research']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ['kemtls']

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: "kemtls-embedded"
---
