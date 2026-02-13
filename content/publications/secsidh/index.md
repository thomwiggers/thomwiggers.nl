---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Optimizations and Practicality of High-Security CSIDH"
authors:
  - Fabio Campos
  - Jorge Chávez-Saab
  - Jesús-Javier Chi-Domínguez
  - Michael Meyer
  - Krijn Reijnders
  - Francisco Rodríguez-Henríquez
  - peterschwabe
  - me
date: 2024-04-09T00:00:00+02:00
hugoblox.ids: {doi: "10.62056/anjbksdja"}

# Schedule page publish date (NOT publication's date).
publishDate: 2023-06-05T16:40:16+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IACR Communications in Cryptology"
publication_short: ""

abstract: |
  In this work, we assess the real-world practicality of CSIDH, an isogeny-based non-interactive key exchange. We provide the first thorough assessment of the practicality of CSIDH in higher parameter sizes for conservative estimates of quantum security, and with protection against physical attacks.

  This requires a three-fold analysis of CSIDH. First, we describe two approaches to efficient high-security CSIDH implementations, based on SQALE and CTIDH. Second, we optimize such high-security implementations, on a high level by improving several subroutines, and on a low level by improving the finite field arithmetic. Third, we benchmark the performance of high-security CSIDH. As a stand-alone primitive, our implementations outperform previous results by a factor up to 2.53×.

  As a real-world use case considering network protocols, we use CSIDH in TLS variants that allow early authentication through a NIKE. Although our instantiations of CSIDH have smaller communication requirements than post-quantum KEM and signature schemes, even our highly-optimized implementations result in too-large handshake latency (tens of seconds), showing that CSIDH is only practical in niche cases.

# Summary. An optional shortened abstract.
summary: >
  We propose higher-security parametersets of CSIDH, and present
  highly-optimized implementations. We measure the performance when using these
  parameters in TLS, and show that the performance is likely not fast enough to
  consider using CSIDH with conservative parmeter sets.

tags: ['research', 'tls', 'post-quantum', 'cryptography']
categories: ['research']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

links: [{type: preprint, url: "https://eprint.iacr.org/2023/793"}]

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
