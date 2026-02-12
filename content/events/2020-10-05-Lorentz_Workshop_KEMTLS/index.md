---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Post-Quantum TLS without handshake signatures"
event: Lorentz Workshop on Post-Quantum Cryptography for Embedded Systems
event_url: https://www.lorentzcenter.nl/post-quantum-cryptography-for-embedded-systems.html
location: Virtual
address:
  street:
  city:
  region:
  postcode:
  country:
summary: Talk about Post-Quantum TLS without Handshake Signatures at the Lorentz Workshop (virtual)
abstract: |
  It's possible to make TLS 1.3 post-quantum secure by just plugging in post-quantum key exchange and a post-quantum signature scheme. But PQ signatures tend to be quite big and slow. KEMTLS is our proposal for a post-quantum secure variant of TLS that authenticates by using KEMs instead of the handshake signature. With a trick to preserve the ability to allow the client to send the request after the server sends its certificate: using KEMs instead of signatures doesn't take more round trips for this first message.
  We compare a few instantiations of KEMTLS. Optimised for communication size, KEMTLS, with SIKE for KEX and handshake authentication, GeMSS for the CA certificate and a custom XMSS for optional intermediate certificates, requires less than half the bandwidth of a post-quantum TLS 1.3 using Falcon for the handshake signature. When picking primitives for speed, KEMTLS reduces the amount of server CPU cycles by up to 90% compared to an equivalent post-quantum instantiation of TLS 1.3, as well as reducing the time before the client can send its first application data.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2020-10-05
date_end: 2020-10-09
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: 2020-10-07T14:57:31+02:00

authors: ['thom']
tags:
  - KEMTLS
  - PQTLS
  - Post-Quantum
  - research

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: "presentation.pdf"

url_code:
url_pdf:
url_video: https://youtu.be/Vgg2ae-4WEQ

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - 'kemtls'
---
