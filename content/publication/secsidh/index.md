---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "On the Practicality of Post-Quantum TLS using Large-Parameter CSIDH"
authors:
  - Fabio Campos
  - Jorge Chávez-Saab
  - Jesús-Javier Chi-Domínguez
  - Michael Meyer
  - Krijn Reijnders
  - Francisco Rodríguez-Henríquez
  - peterschwabe
  - thom
date: 2023-06-05T16:40:16+02:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2023-06-05T16:40:16+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "In submission"
publication_short: ""

abstract: >
  The isogeny-based scheme CSIDH is considered to be the only efficient post-quantum non-interactive key exchange (NIKE) and poses small bandwidth requirements, thus appearing to be an attractive alternative for classical Diffie–Hellman schemes.
  A crucial CSIDH design point, still under debate, is its quantum security when using prime fields of 512 to 1024 bits.
  Most work has focused on prime fields of that size and the practicality of CSIDH with large parameters, 2000 to 9000 bits, has so far not been thoroughly assessed, even though analysis of quantum security suggests these parameter sizes.
  We fill this gap by providing two CSIDH instantiations: A deterministic and dummy-free instantiation based on SQALE, aiming at high security against physical attacks, and a speed-optimized constant-time instantiation that adapts CTIDH to larger parameter sizes.
  We provide implementations of both variants, including efficient field arithmetic for fields of such size, and high-level optimizations. Our deterministic and dummy-free version, dCSIDH, is almost twice as fast as SQALE, and, dropping determinism, CTIDH at these parameters is thrice as fast as dCSIDH.
  We investigate their use in real-world scenarios through benchmarks of TLS using our software.
  Although our instantiations of CSIDH have smaller communication requirements than post-quantum KEM and signature schemes, both implementations still result in too-large handshake latency (tens of seconds), which hinder further consideration of using CSIDH in practice for conservative parameter set instantiations.

# Summary. An optional shortened abstract.
summary: "We propose higher-security parametersets of CSIDH, and present highly-optimized implementations. We measure the performance when using these parameters in TLS, and show that the performance is likely not fast enough to consider using CSIDH with conservative parmeter sets."

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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
