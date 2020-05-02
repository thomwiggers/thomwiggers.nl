---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

profile: false

title: "Post-Quantum TLS without handshake signatures"
authors:
  - peterschwabe
  - douglasstebila
  - thom
date: 2020-05-04
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2020-05-04T14:00:00+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "Post-Quantum TLS without handshake signatures"
publication_short: ""

abstract: "todo"

# Summary. An optional shortened abstract.
summary: |
  We present an alternative to TLS 1.3, by authenticating using only Key-Encapsulation Mechanisms.
  This allows us to get rid of handshake signatures, as post-quantum signature schemes are expensive,
  both in bytes and computation times.

tags:
  - cryptography
  - post-quantum
  - tls
  - key-encapsulation mechanisms
  - kemtls
categories:
  - research
  - tls
  - security
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
projects: ['kem-tls']

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

Submitted to ACM CCS


## Software

Software that accompanies this publication can be found at [Github](https://github.com/thomwiggers/kemtls-experiment/).
