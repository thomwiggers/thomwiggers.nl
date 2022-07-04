---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "KEMTLS with Delayed Forward Identity Protection in (Almost) a Single Round"
authors:
  - Felix Günther
  - Simon Rastikian
  - Patrick Towa
  - thom


date: 2022-06-18T16:20:10+02:00
doi: "10.1007/978-3-031-09234-3_13"

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-24T16:20:10+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "ACNS 2022"
publication_short: ""

abstract: |
  The recent KEMTLS protocol (Schwabe, Stebila and Wiggers,CCS’20) is a promising design for a quantum-safe TLS handshake protocol. Focused on the web setting, wherein clients learn server public-key certificates only during connection establishment, a drawback of KEMTLS compared to TLS 1.3 is that it introduces an additional round trip before the server can send data, and an extra one for the client as well in the case of mutual authentication. In many scenarios, including IoT and embedded settings, client devices may however have the targeted server certificate pre-loaded, so that such performance penalty seems unnecessarily restrictive.

  This work proposes a variant of KEMTLS tailored to such scenarios. Our protocol leverages the fact that clients know the server public keys in advance to decrease handshake latency while protecting client identities. It combines medium-lived with long-term server public keys to enable a delayed form of forward secrecy even from the first data flow on, and full forward secrecy upon the first round trip. The new protocol is proved to achieve strong security guarantees, based on the security of the underlying building blocks, in a new model for multi-stage key exchange with medium-lived keys.

# Summary. An optional shortened abstract.
summary: ""

tags:
  - KEMTLS
  - research
  - kemtls-epoch
categories: 
  - kemtls
  - research
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_preprint: https://eprint.iacr.org/2021/725
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

