---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Verifying Post Quantum Signatures in 8kB of RAM"
authors:
  - Ruben Gonzalez
  - Andreas Hülsing
  - Matthias J. Kannwischer
  - Juliane Krämer
  - Tanja Lange
  - Marc Stöttinger
  - Elisabeth Waitz
  - thom
  - Bo-Yin Yang
date: 2021-05-25T09:43:12+02:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2021-05-25T09:43:12+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "PQCrypto 2021"
publication_short: ""

abstract: |
  In this paper, we study implementations of post-quantum signature schemes on
  resource-constrained devices. We focus on verification of signatures and
  cover NIST PQC round-3 candidates Dilithium, Falcon, Rainbow, GeMSS, and
  SPHINCS+. We assume an ARM Cortex-M3 with 8 kB of memory and 8 kB of flash for
  code; a practical and widely deployed setup in, for example, the automotive
  sector. This amount of memory is insufficient for most schemes. Rainbow and
  GeMSS public keys are too big; SPHINCS+ signatures do not fit in this memory.
  To make signature verification work for these schemes, we stream in public
  keys and signatures. Due to the memory requirements for efficient Dilithium
  implementations, we stream in the public key to cache more intermediate
  results. We discuss the suitability of the signature schemes for streaming,
  adapt existing implementations, and compare performance.

# Summary. An optional shortened abstract.
summary: ""

tags:
  - research
  - post-quantum
  - cryptography
categories:
  - research
  - post-quantum
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_preprint: https://eprint.iacr.org/2021/662
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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
To appear at PQCrypto 2021
