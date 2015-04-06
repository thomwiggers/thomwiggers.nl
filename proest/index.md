---
layout: default
status: publish
published: true
title: Bachelor Thesis
author: Thom Wiggers
author_login: Thom Wiggers
author_url: https://thomwiggers.nl
date: '2015-03-29'
tags:
    - cryptography
    - proest
    - research
    - thesis
---

# Prøst

Prøst is an authenticated encryption cipher and a contestant in the [CAESAR][caesar] competition for Authenticated Encryption.
For my bachelor thesis research project, I've implemented Prøst on ARM11.

## Thesis

My thesis was titled [Implementing Prøst on ARM11][thesis]. The presentation can be [found here][presentation].

## Software

* Prøst on ARM can be [found on Github here][proest-arm11]
* My implementation of the Shortest Straight Line program finder is also [available on github][slpsat]
* My modified version of [qhasm][qhasm] is also [available on github][qhasm-arm]. The no-stack version is available from the branch `nostack`.
* My implementation of Boyar's heuristic for finding shorter straight line programs [can be found here][slp-heuristic].
* My packaged version of `cpucycles4ns` can be found at [github][cpucycles4ns]
* The LaTeX source code for the documents I've produced is [available here][fixme]

[qhasm-arm]: https://github.com/thomwiggers/qhasm
[slpsat]: https://github.com/thomwiggers/find-shortest-slp
[slp-heuristic]: https://github.com/thomwiggers/slp-heuristic
[proest-arm11]: https://github.com/thomwiggers/proest-arm11
[thesis]: bachelorthesis.pdf
[presentation]: presentation.pdf
[caesar]: http://competitions.cr.yp.to
[qhasm]: http://cr.yp.to/qhasm.html
[cpucycles4ns]: https://github.com/thomwiggers/cpucycles4ns
[fixme]: http://wpformation.com/wp-content/uploads/2014/03/todo1.jpg
