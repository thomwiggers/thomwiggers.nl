---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "More efficient post-quantum KEMTLS with pre-distributed public keys"
authors:
  - peterschwabe
  - douglasstebila
  - thom
date: 2021-09-30
doi: "10.1007/978-3-030-88418-5_1"

# Schedule page publish date (NOT publication's date).
publishDate: 2021-05-12T19:37:15+02:00
lastmod: 2021-10-05T10:56:00+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "ESORICS 2021"
publication_short: ""

abstract: |
  While server-only authentication with certificates is the most widely used mode of operation for the Transport Layer Security (TLS) protocol on the world wide web, there are many applications where TLS is used in a different way or with different constraints.
  For example, embedded Internet-of-Things clients may have a server certificate pre-programmed and be highly constrained in terms of communication bandwidth or computation power.
  As post-quantum algorithms have a wider range of performance trade-offs, designs other than traditional “signed-key-exchange” may be worthwhile.
  The KEMTLS protocol, presented at ACM CCS 2020, uses key encapsulation mechanisms (KEMs) rather than signatures for authentication in the TLS 1.3 handshake, a benefit since most post-quantum KEMs are more efficient than PQ signatures.
  However, KEMTLS has some drawbacks, especially in the client authentication scenario which requires a full additional roundtrip.

  We explore how the situation changes with _pre-distributed public keys_, which may be viable in many scenarios, for example pre-installed public keys in apps, on embedded devices, cached public keys, or keys distributed out of band.
  Our variant of KEMTLS with pre-distributed keys, called KEMTLS-PDK, is more efficient in terms of both bandwidth and computation compared to post-quantum signed-KEM TLS (even cached public keys), and has a smaller trusted code base.
  When client authentication is used, KEMTLS-PDK is more bandwidth efficient than  KEMTLS yet can complete client authentication in one fewer round trips, and has stronger authentication properties.
  Interestingly, using pre-distributed keys in KEMTLS-PDK changes the landscape on suitability of PQ algorithms: schemes where public keys are larger than ciphertexts/signatures (such as Classic McEliece and Rainbow) can be viable, and the differences between some lattice-based schemes is reduced.
  We also discuss how using pre-distributed public keys provides privacy benefits compared to pre-shared symmetric keys in TLS.


# Summary. An optional shortened abstract.
summary: >
  We make KEMTLS more efficient in scenarios where the client already has the server's
  long-term public key, for example through caching or because it's pre-installed.

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
url_preprint: https://eprint.iacr.org/2021/779

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

## Proof

The full version is linked above.

## Software

The implementation can be found [on Github](https://github.com/thomwiggers/kemtls-experiment/tree/reimplementation).
