---
# Documentation: https://docs.hugoblox.com/managing-content/

title: |
  Comprehensive Deniability Analysis of Signal Handshake Protocols: X3DH, PQXDH
  to Fully Post-Quantum with Deniable Ring Signatures
authors:
- shuichi
- guilhem
- Ida Tucker
- thom
date: 2025-08-15T11:00:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-08-15T14:17:10-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "USENIX Security '25"
publication_short: ""

abstract: |
  The Signal protocol relies on a handshake protocol, formerly X3DH and now PQXDH, to set up secure conversations. One of its privacy properties, of value to Signal, is deniability, allowing users to deny participation in communications. Prior analyses of deniability for these protocols, including post-quantum variants, use models highly tailored to the individual protocols and generally make ad-hoc adaptations to "standard" AKE definitions, obscuring the concrete deniability guarantees and complicating comparisons across protocols. Building on Hashimoto et al.'s abstraction for Signal handshake protocols (USENIX '25), we address this gap by presenting a unified framework for analyzing their deniability.

  We analyze Signal's classically secure X3DH and harvest-now-decrypt-later-secure PQXDH, and show that PQXDH is deniable against harvest-now-judge-later attacks, where a quantum judge retrospectively assesses the participation of classical users. We further analyze post-quantum alternatives like RingXKEM, whose deniability relies on ring signatures (RS). By introducing a novel metric inspired by differential privacy, we provide relaxed, pragmatic guarantees for deniability. We also use this metric to define deniability for RS, a relaxation of anonymity, allowing us to build an efficient RS from NIST-standardized Falcon (and MAYO), which is not anonymous, but is provably deniable.

# Summary. An optional shortened abstract.
summary: ""

tags: ['signal', 'ringxkem', 'deniability', 'cryptography']
categories: ['signal']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://eprint.iacr.org/2025/1090.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
url_preprint: https://eprint.iacr.org/2025/1090

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
Appeared in [USENIX Security '25](https://www.usenix.org/conference/usenixsecurity25/presentation/katsumata)
