---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Post-Quantum TLS with KEMs"
summary: "We investigate getting rid of signatures in TLS"
authors: ['me']
tags: 
  - cryptography
  - post-quantum
  - key-encapsulation mechanisms
  - KEM
  - TLS
categories: ['research', 'security']
date: 2020-05-02T13:41:11+02:00

# Optional external URL for project (replaces project detail page).
external_link: ""

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


# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

aliases:
  - /project/kem-tls/
---

We investigate alternate ways to bring TLS into the post-quantum age.
Notably, we try to get rid of the expensive signature schemes in the online handshake, by authenticating using only KEMs.
This research is the main subject of my [PhD thesis]({{< relref "/publications/thesis" >}}).
