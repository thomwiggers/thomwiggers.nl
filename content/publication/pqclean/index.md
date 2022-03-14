---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Improving Software Quality in Cryptography Standardization Projects"
authors:
  - "matthiaskannwischer"
  - "peterschwabe"
  - "douglasstebila"
  - "thom"
date: 2022-03-14T14:58:33+01:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-03-14T14:58:33+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: |
  The NIST post-quantum cryptography (PQC) standardization project is probably
  the largest and most ambitious cryptography standardization effort to date, and
  as such it makes an excellent case study of cryptography standardization
  projects. It is expected that with the end of round 3 in early 2022, NIST will
  announce the first set of primitives to advance to standardization, so it seems
  like a good time to look back and see what lessons can be learned from this
  effort. In this paper, we take a look at one specific aspect of the NIST PQC
  project: software implementations. We observe that many implementations
  included as a mandatory part of the submission packages were of poor quality
  and ignored decades-old standard techniques from software engineering to
  guarantee a certain baseline quality level. As a consequence, it was not
  possible to readily use those implementations in experiments for post-quantum
  protocol migration and software optimization efforts without first spending
  a significant amount of time to clean up the submitted reference
  implementations.

  We do not mean to criticize cryptographers who submitted proposals, including
  software implementations, to NIST PQC: after all, it cannot reasonably be
  expected from every cryptographer to also have expertise in software
  engineering. Instead, we suggest how standardization bodies like NIST can
  improve the software-submission process in future efforts to avoid such issues
  with submitted software. More specifically, we present PQClean, an extensive
  (continuous-integration) testing framework for PQC software, which now also
  contains "clean" implementations of the NIST round 3 candidate schemes. We
  argue that the availability of such a framework---either in an online
  continuous-integration setup, or just as an offline testing system---long
  before the submission deadline would have resulted in much better
  implementations included in NIST PQC submissions and overall would have saved
  the community and probably also NIST a lot of time and effort.

# Summary. An optional shortened abstract.
summary: ""

tags: ['post-quantum cryptography']
categories: ['research']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_preprint: https://eprint.iacr.org/2022/337
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
