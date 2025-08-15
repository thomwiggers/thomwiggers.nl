---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "Bundled Authenticated Key Exchange: A Concrete Treatment of (Post-Quantum) Signal's Handshake Protocol"
authors:
- shuichi
- thom
- keitaro
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
  The Signal protocol relies on a special handshake protocol, formerly X3DH and
  now PQXDH, to set up secure conversations. Prior analysis of these protocols
  (or proposals for post-quantum alternatives) have all used highly tailored
  models to the individual protocols and generally made ad-hoc adaptations to
  "standard" AKE definitions, making the concrete security attained unclear and
  hard to compare. Indeed, we observe that some natural Signal handshake
  protocols cannot be handled by these tailored models. In this work, we
  introduce Bundled Authenticated Key Exchange (BAKE), a concrete treatment of
  the Signal handshake protocol. We formally model prekey bundles and states,
  enabling us to define various levels of security in a unified model. We analyze
  Signal's classically secure X3DH and harvest-now-decrypt-later-secure PQXDH,
  and show that they do not achieve what we call optimal security (as is
  documented). Next, we introduce RingXKEM, a fully post-quantum Signal handshake
  protocol achieving optimal security; as RingXKEM shares states among many
  prekey bundles, it could not have been captured by prior models. Lastly, we
  provide security and efficiency comparison of X3DH, PQXDH, and RingXKEM.

# Summary. An optional shortened abstract.
summary: ""

tags: ['signal', 'ake', 'cryptography']
categories: ['signal']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://eprint.iacr.org/2025/040.pdf
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:
url_preprint: https://eprint.iacr.org/2025/040

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
Appeared in [USENIX Security '25](https://www.usenix.org/conference/usenixsecurity25/presentation/hashimoto-key-exchange)
