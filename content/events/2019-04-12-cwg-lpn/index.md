---
title: "Solving LPN Using Large Covering Codes"
date: 2019-04-08T10:45:00+01:00
all_day: false
publishDate: 2019-04-08
authors: ["me"]
location: "Utrecht, The Netherlands"
event: "Crypto Working Group 2019-04-12"
event_url: "https://www.win.tue.nl/eipsi/seminars_cwg.html"
abstract: |
  Since quantum computers are expected to break most of the cryptographic schemes we rely on today, we need to look at alternatives. Learning
  Parity with Noise (LPN) is mathematical problem that we can base cryptographic schemes on, and it is supposed to be hard for both
  classical and quantum computers. We will be looking at how hard this problem actually is, by studying existing attacks on the LPN problem.
  Most attacks on LPN use enormous amounts of memory. We aim to improve that situation.

  More concretely, we study composing a reduction based on covering codes with a solving algorithm called Gauss. Both the reduction and the Gauss
  algorithm use little memory, but by itself Gauss is slower than attacks that use more memory.

  Unfortunately, we determine that this combination will not work. We also look at improving the codes used by the reduction by applying StGen
  codes, which was proposed by simonasamardjiska at a DS lunch talk in March 2017. While this improves run-time performance in theory, the
  real-world performance is much less positive.

  Finally, we developed software that we hope allows people to easily work with the LPN problem and the algorithms that aim to solve it.
summary: ""
featured: false
tags: ["lpn", "post-quantum cryptography", "cryptography", "academic"]
slides: ""
links:
  - type: slides
    url: "presentation.pdf"
projects: []
image:
  caption: ""
  focal_point: ""
---
