---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Implementing and Measuring KEMTLS"
authors:
  - sofiaceli
  - Armando Faz-Hernández
  - Nick Sullivan
  - Goutam Tamvada
  - Luke Valenta
  - Bas Westerbaan
  - thom
  - Christopher Wood
date: 2021-09-30
doi: "10.1007/978-3-030-88238-9_5"

# Schedule page publish date (NOT publication's date).
publishDate: 2021-07-05T11:42:25+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "Progress in Cryptology — Latincrypt 2021"
publication_short: "Latincrypt 2021"

abstract: |
  KEMTLS (CCS 2020) is a novel alternative to the Transport Layer Security (TLS) handshake that integrates post-quantum algorithms.
  It uses a key encapsulation mechanism (KEM) for both confidentiality and authentication, achieving post-quantum security while obviating the need for expensive post-quantum signatures. The original KEMTLS paper presents a security analysis, Rust implementation, and benchmarks over emulated networks.
  In this work, we provide full Go implementations of KEMTLS and several other post-quantum handshake alternatives, describe our integration into a real distributed system, and provide performance evaluations over real network conditions.
  We compare the standard (non-quantum-resistant) TLS 1.3 handshake with three alternatives: one that uses post-quantum signatures in combination with a KEM (PQTLS), one fully KEM application (KEMTLS), and a reduced round trip version (KEMTLS-PDK).
  In addition to the performance evaluations, we discuss how the design of these protocols impacts TLS from an implementation and configuration perspective.

# Summary. An optional shortened abstract.
summary: ""

tags:
  - research
  - tls
  - KEMTLS
  - cloudflare
  - post-quantum cryptography
  - PQTLS
categories:
  - research
  - cryptography
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_preprint: "https://eprint.iacr.org/2021/1019"
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
projects: ["kemtls"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

