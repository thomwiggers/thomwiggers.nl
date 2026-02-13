---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "TLS → Post-Quantum TLS: Inspecting the TLS landscape for PQC adoption on Android"
authors: ['Dimitri Mankowski', 'me', 'Veelasha Moonsamy']
date: 2023-07-07T16:01:22+02:00
hugoblox.ids: {doi: "10.1109/EuroSPW59978.2023.00065"}

# Schedule page publish date (NOT publication's date).
publishDate: 2023-06-05T16:01:22+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "International Workshop on Traffic Measurements for Cybersecurity"
publication_short: "WMTC 2023"

abstract: >
    The ubiquitous use of smartphones has contributed to more and more users conducting their online browsing activities through apps, rather than web browsers. In order to provide a seamless browsing experience to the users, apps rely on a variety of HTTP-based APIs and third-party libraries, and make use of the TLS protocol to secure the underlying communication. With NIST's recent announcement of the first standards for post-quantum algorithms, there is a need to better understand the constraints and requirements of TLS usage by Android apps in order to make an informed decision for migration to the post-quantum world.

    In this paper, we performed an analysis of TLS usage by highest-ranked apps from Google Play Store to assess the resulting overhead for adoption of post-quantum algorithms. Our results show that apps set up large numbers of TLS connections with a median of 94, often to the same hosts. At the same time, many apps make little use of resumption to reduce the overhead of the TLS handshake. This will greatly magnify the impact of the transition to post-quantum cryptography, and we make recommendations for developers, server operators and the mobile operating systems to invest in making more use of these mitigating features or improving their accessibility. Finally, we briefly discuss how alternative proposals for post-quantum TLS handshakes might reduce the overhead.

# Summary. An optional shortened abstract.
summary: ""

tags: ['kemtls', 'research', 'post-quantum cryptography', 'apps']
categories: ['research']
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

links:
  - type: preprint
    url: "https://eprint.iacr.org/2023/734"
  - type: code
    url: "https://zenodo.org/record/7950522"
  - type: dataset
    url: "https://zenodo.org/record/7950522"

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

