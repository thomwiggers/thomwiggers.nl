---
# Publication title
title: "Solving LPN using Large Covering Codes"

# Date first published.
date: "2018-09-25"

# Authors
authors:
  - thom

# Publication type
# 0: Uncategorized
# 1: Conference paper
# 2: Journal article
# 3: Manuscript
# 4: Report
# 5: Book
# 6: Book section
publication_types:
  - 7

# Publication name and optional abbreviated version
# i.e. published in
publication: "Master's thesis"
#publication_short = "In *ICA*"

# Abstract and optional short version
abstract: |
  Learning Parity with Noise (LPN) is a computational problem that we
  can use for cryptographic algorithms. It is suspected that LPN can not be
  solved (much) more efficiently on a quantum computer than on a classic machine.
  The most time-efficient solving algorithms for LPN use as much memory as they
  need time. The amount of memory needed may be a more limiting factor for
  practical attacks than the time that would be spent. We propose to improve the
  theoretical performance of algorithms that use a reduction based on covering
  codes. By applying the StGen codes proposed by Samardjiska and Gligoroski, we
  are able to create codes that have a better bias. However, we also show that it
  is important to consider the time needed to decode such codes. We also study
  the Gauss solving algorithm, proposed by Esser, Kübler and May. It does not
  have the best performance, but it is able to solve LPN problems using small
  amounts of memory. We combine it with the code reduction to obtain a solving
  algorithm we will refer to as Coded Gauss. This combination should not consume
  too much memory and provide better performance than Gauss. Unfortunately, by
  applying the theoretical bounds of covering codes, we show that this
  combination will not work. Coded Gauss would be a less efficient algorithm than
  applying Gauss to the full problem. We also show that there do exist some
  edge-case scenarios where Coded Gauss may still be faster than Gauss, but would
  consume about as much memory as faster solving algorithms. Finally, we present
  a software implementation of algorithms that reduce and solve LPN problems.
  This software is easily adaptable to any attack on an LPN problem to study
  their behaviour. We hope that the software is helpful for people trying to
  understand the LPN problem and the many proposed algorithms.

# Featured image
#image_preview = ""

# Is this a selected publication (true/false)
#selected = true

# Associated projects
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
#projects = []

# Links
url_pdf: "pdf/msc/thesis.pdf"
url_preprint: ""
url_code: ""
url_dataset: ""
url_project: ""
url_slides: ""
url_video: ""
url_poster: ""
url_source: ""

# DOI
doi: ""

# Custom links (optional)
# url_custom: [{name = "Custom Link", url = "http://example.org"}]

# Do we use Maths
math: false

# Do we need source code highlighting
highlight: false

# Featured image
#[header]
#image: "headers/bubbles-wide.jpg"
#caption: "My caption

aliases:
  - 'research/msc-thesis/'
---

Master's thesis written under the supervision of Simona Samardjiska.

## Software

* The Rust bindings for M4RI can be found on [crates.io][m4ri-crate] and [Github][m4ri-github].
* The implementations of attacks on LPN can be found on [crates.io][lpn-crate] and [Github][lpn-github] ([documentation][lpn-docs]).


[m4ri-crate]: https://crates.io/crates/m4ri-rust
[m4ri-github]: https://github.com/thomwiggers/m4ri-rust/
[lpn-github]: https://github.com/thomwiggers/lpn/
[lpn-crate]: https://crates.io/crates/lpn
[lpn-docs]: https://docs.rs/lpn/
