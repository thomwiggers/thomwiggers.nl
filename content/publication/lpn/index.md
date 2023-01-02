---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Practically Solving LPN"
authors:
  - thom
  - simonasamardjiska
date: 2021-07-12
doi: "10.1109/ISIT45174.2021.9518109"

# Schedule page publish date (NOT publication's date).
publishDate: 2021-02-06T11:14:42+01:00
lastmod: 2021-02-10

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE International Symposium on Information Theory 2021"
publication_short: "IEEE ISIT 2021"

abstract: |
   The best algorithms for the Learning Parity with Noise (LPN) problem require sub-exponential time and memory.
   This often makes memory, and not time, the limiting factor for practical attacks, which seem to be out of reach even for relatively small parameters.
   In this paper, we try to bring the state-of-the-art in solving LPN closer to the practical realm.
   We improve upon the existing algorithms by modifying the Coded-BKW algorithm to work under various memory constrains.
   We correct and expand previous analysis and experimentally verify our findings.
   As a result we were able to mount practical attacks on the largest parameters reported to date using only $2^{39}$ bits of memory.

# Summary. An optional shortened abstract.
summary: "We analyse the difficulty of the LPN problem in restricted memory."

tags: ["lpn", "post-quantum cryptography", "cryptography", "cryptanalysis"]
categories: ["cryptography", "research"]
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_preprint: "https://eprint.iacr.org/2021/962"
url_code: "/publication/lpn/#software"
url_dataset: "/publication/lpn/#chains-found-by-our-algorithm"
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

Accepted at IEEE ISIT 2021.

Part of this work originally appeared in my [master's thesis][]

[master's thesis]: {{< relref "masters-thesis" >}}

## Software

### LPN cryptanalysis implementations

We have an efficient software implementation in Rust that allows to compose attacks on LPN.
It is [available from github][lpn software].

[lpn software]: https://github.com/thomwiggers/lpn/

### Efficient LPN chain finding algorithm

We hope to make our implementation available soon — it requires a bit of cleanup.
Contact us if you want earlier access.

### Chains found by our algorithm

We need to document the output format before we make this available.
Contact us if you want earlier access.

