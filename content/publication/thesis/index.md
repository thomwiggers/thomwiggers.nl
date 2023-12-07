---
# Documentation: https://wowchemy.com/docs/managing-content/


title: "Post-Quantum TLS"
authors: ['thom']
date: 2024-01-09T14:30:00+01:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2023-05-01T16:01:22+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["thesis"]

# Publication name and optional abbreviated publication name.
publication: "Radboud University"
publication_short: ""

abstract: >
  Ph.D. thesis on post-quantum cryptography in TLS.
  I investigate current proposals for post-quantum TLS,
  but more importantly we propose a more efficient TLS
  handshake that makes use of trade-offs presented by
  post-quantum cryptographic primitives (which were not
  as profound in pre-quantum primitives).
  This more efficient protocol we call KEMTLS.
  Benchmarks in several different settings for all variants
  of post-quantum TLS show that KEMTLS is efficient, and
  we also have an extensive analysis of the security of KEMTLS.

# Summary. An optional shortened abstract.
summary: ""

tags: ['kemtls', 'research']
categories: ['research']
featured: true

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

You can [find information on the defense here]({{< ref "/event/phd-defense" >}}).


## Software and raw data

* [Post-Quantum TLS experiments](https://github.com/thomwiggers/kemtls-experiment/tree/thesis/)
* [KEMTLS in Tamarin]({{< ref "/publication/kemtls-tamarin" >}})
* [KEMTLS over the internet]({{< ref "/publication/measuring-kemtls" >}})
* [KEMTLS on embedded systems]({{< ref "/publication/kemtls-embedded" >}})
* [PQClean](https://github.com/PQClean/PQClean)
* [Verifying post-quantum signatures in 8kB of RAM]({{< ref "/publication/verifying-post-quantum-signatures-in-8kb-of-ram" >}})
* [Practially solving LPN]({{< ref "/publication/lpn" >}})
