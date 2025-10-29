---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "Revisiting PQ WireGuard: A Comprehensive Security Analysis With a New Design Using Reinforced KEMs"
authors: 
  - Keitaro Hashimoto
  - Shuichi Katsumata
  - Guilhem Niot
  - Thom Wiggers
date: 2026-05-18T08:00:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-10-29T11:35:38+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Security & Privacy 2026"
publication_short: "IEEE S&P 2026"

abstract: >
  WireGuard is a VPN based on the Noise protocol, known for its high
  performance, small code base, and unique security features. Recently, Hülsing
  et al. (IEEE S&P'21) presented post-quantum (PQ) WireGuard, replacing the
  Diffie-Hellman (DH) key exchange underlying the Noise protocol with
  key-encapsulation mechanisms (KEMs). Since WireGuard requires the handshake
  message to fit in one UDP packet of size roughly 1200 B, they combined
  Classic McEliece and a modified variant of Saber. However, as Classic
  McEliece public keys are notoriously large, this comes at the cost of
  severely increasing the server's memory requirement. This hinders deployment,
  especially in environments with constraints on memory (allocation), such as
  a kernel-level implementations.

  In this work, we revisit PQ WireGuard and improve it on three fronts: design,
  (computational) security, and efficiency. As KEMs are semantically, but not
  syntactically, the same as DH key exchange, there are many (in hindsight)
  ad-hoc design choices being made, further amplified by the recent finding on
  the binding issues with PQ KEMs (Cremers et al., CCS'24). We redesign PQ
  WireGuard addressing these issues, and prove it secure in a new computational
  model by fixing and capturing new security features that were not modeled by
  Hülsing et al. We further propose 'reinforced KEM' (RKEM) as a natural building
  block for key exchange protocols, enabling a PQ WireGuard construction where
  the server no longer needs to store Classical McEliece keys, reducing public
  key memory by 190 to 390×. In essence, we construct a RKEM named 'Rebar' to
  compress two ML-KEM-like ciphertexts which may be of an independent interest.

# Summary. An optional shortened abstract.
summary: >
  WireGuard is a VPN protocol with an efficient, DH-based handshake. Prior
  attempts at making it PQ heavily relied on Classic McEliece, which has
  deployment complications. We revisit PQ WireGuard and manage to get rid of
  one of the uses of Classic McEliece by providing optimized KEMs.  We also fix
  a flaw in the security of post-quantum WireGuard, which assumed KEM binding
  properties not necessarily provided by Classic McEliece.

tags: ['protocols', 'post-quantum', 'wireguard']
categories: ['post-quantum']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_preprint: https://eprint.iacr.org/2025/1758
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
