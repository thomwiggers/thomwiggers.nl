---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "A Comprehensive Study of the Signal Handshake Protocol: Bundled Authenticated Key Exchange"
authors:
  - keitaro
  - shuichi
  - guilhem
  - Ida Tucker
  - thom
date: 2025-09-28
hugoblox.ids: {doi: ""}

# Schedule page publish date (NOT publication's date).
publishDate: 2025-10-29T11:48:20+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "6th NIST PQC Standardization Conference"
publication_short: "NIST PQC Conference"

abstract: >
  The Signal protocol relies on a special handshake protocol, formerly X3DH and
  now PQXDH, to set up secure conversations. One of its privacy properties, of
  value to Signal, is _deniability_, allowing users to deny participation in
  communications. Prior analyses of these protocols (or proposals for
  post-quantum alternatives) have all used highly tailored models to the
  individual protocols and generally made ad-hoc adaptations to "standard" AKE
  definitions, making the concrete security attained unclear and hard to compare
  between similar protocols. Indeed, we observe that some natural Signal
  handshake protocols cannot be handled by these tailored models. In this work,
  we introduce _Bundled Authenticated Key Exchange_ (BAKE), a concrete
  treatment of the Signal handshake protocol. We formally model prekey
  _bundles_ and states, enabling us to define various levels of security in
  a unified model, along with a framework for analyzing deniability. We analyze
  Signal's classically secure X3DH and
  _harvest-now-decrypt-later_-secure PQXDH, and show that they do not
  achieve what we call _optimal_ security (as is documented). Regarding
  deniability, we show that PQXDH is deniable against
  harvest-now-_judge_-later attacks, where a quantum judge retrospectively
  assesses the participation of classical users. Next, we introduce RingXKEM,
  a fully post-quantum Signal handshake protocol achieving optimal security; as
  RingXKEM shares states among many prekey bundles, it could not have been
  captured by prior models. Motivated by our deniability analysis of RingXKEM
  we introduce a novel metric inspired by differential privacy, providing
  relaxed, pragmatic guarantees for deniability. We also use this metric to
  define _deniability_ for RS, a relaxation of anonymity, allowing us to
  build an efficient RS from NIST-standardized Falcon (and MAYO), which is not
  anonymous, but is provably deniable. Lastly, we provide security, deniability
  and efficiency comparisons of X3DH, PQXDH, and RingXKEM.



# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

links: [{type: slides, url: "slides.pdf"}]

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

Ida Tucker presented this paper at the [NIST PQC Conference][]. Her [slides are available here](slides.pdf)


[NIST PQC Conference]: https://csrc.nist.gov/Events/2025/6th-pqc-standardization-conference
