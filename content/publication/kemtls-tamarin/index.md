---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A tale of two models: formalizing KEMTLS in Tamarin"
authors:
  - "sofiaceli"
  - "Jonathan Hoyland"
  - "douglasstebila"
  - "thom"
date: 2022-05-18T11:33:09+02:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-18T11:33:09+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "A tale of two models: formalizing KEMTLS in Tamarin"
publication_short: "Formalizing KEMTLS in Tamarin"

abstract: |
  KEMTLS is a proposal for changing the TLS handshake to authenticate the
  handshake using long-term key encapsulation mechanism keys instead of
  signatures, motivated by trade-offs in the characteristics of post-quantum
  algorithms. Proofs of the security of KEMTLS and its variant KEMTLS-PDK have
  previously been done manually in the reductionist model under computational
  assumptions. In this paper, we present analyses of KEMTLS and KEMTLS-PDK
  using two distinct Tamarin models. In the first analysis, we adapt the
  extensive Tamarin model of TLS 1.3 of Cremers et al. (ACM CCS 2017) to
  KEMTLS(-PDK); this model closely follows the wire-format of the protocol
  specification. We show that KEMTLS(-PDK) has the same security properties as
  TLS 1.3 in this model. We were able to fully automate this Tamarin proof,
  compared with the previous TLS 1.3 Tamarin model, which requires a big manual
  proving effort; we also uncovered some inconsistencies in the previous model.
  In the second analysis, we present a novel Tamarin model of KEMTLS(-PDK),
  which closely follows the "multi-stage key exchange" security model in the
  pen-and-paper proof of KEMTLS(-PDK). The second approach is further away from
  the wire-format of the protocol specification but captures more subtleties in
  security definitions, like deniability and different levels of forward
  secrecy; it also identifies some flaws in the security claims from the
  pen-and-paper proofs. Our positive security results increase the confidence
  in the design of KEMTLS(-PDK). Moreover, viewing these models side-by-side
  allows us to comment on the trade-off in symbolic analysis between detail in
  protocol specification and granularity of security properties.

# Summary. An optional shortened abstract.
summary: |
  We prove the security of KEMTLS in two Tamarin models.
  One mode is based on the Cremers et al. model of TLS 1.3;
  the other closely resembles our pen-and-paper proofs.
  These models allow us to analyse KEMTLS, and its extension KEMTLS-PDK from different angles.

tags:
  - KEMTLS
  - tamarin
  - research
  - post-quantum cryptography
  - cryptography
categories: ['Post-Quantum', 'Research']
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
slides: ""
---

**This paper is currently in the process of being submitted.**

## Artefacts

* The Tamarin model based on the Cremers et al. model:
    * [Model and proofs](https://github.com/thomwiggers/TLS13Tamarin)
* The Tamarin model that closely resembles our pen-and-paper proofs:
    * [Model and proofs](https://github.com/dstebila/KEMTLS-Tamarin)
