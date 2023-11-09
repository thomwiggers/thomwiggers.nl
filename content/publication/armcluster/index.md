+++
# Page title
title = "Energy-efficient ARM64 Cluster with Cryptanalytic Applications: 80 cores that do not cost you an ARM and a leg"

# Date first published.
date = "2019-06-20"

# Authors
authors = ["thom"]

# Publication type
# 0: Uncategorized
# 1: Conference paper
# 2: Journal article
# 3: Manuscript
# 4: Report
# 5: Book
# 6: Book section
publication_types = ["paper-conference"]

# Publication name and optional abbreviated version
# i.e. published in
publication = "Progress in Cryptology -- LATINCRYPT 2017"
publication_short = "LATINCRYPT 2017"

# Abstract and optional short version
abstract = """Getting a lot of CPU power used to be an expensive under-taking.
  Servers with many cores cost a lot of money and consume large amounts of energy.
  The developments in hardware for mobile devices has resulted in a surge in relatively cheap, powerful, and low-energy CPUs.
  In this paper we show how to build a low-energy, eighty-core cluster built around twenty ODROID-C2 development boards for under 1500 USD.
  The ODROID-C2 is a 46 USD microcomputer that provides a 1.536 GHz quad-core Cortex-A53-based CPU and 2 GB of RAM.
  We investigate the cluster’s application to cryptanalysis by implementing Pollard’s Rho method to tackle the Certicom ECC2K-130 elliptic curve challenge.
  We optimise software from the Breaking ECC2K-130 technical report for the Cortex-A53.
  To do so, we show how to use microbenchmarking to derive the needed instruction characteristics which ARM neglected to document for the public.
  The implementation of the ECC2K-130 attack finally allows us to compare the proposed platform to various other platforms, including “classical” desktop CPUs, GPUs and FPGAs.
  Although it may still be slower than for example FPGAs, our cluster still provides a lot of value for money."""
abstract_short = "Doing cryptanalysis on  a small cluster built from 20 ODROID-C2 boards for under 1500 USD."

# Featured image 
#image_preview = ""

# Is this a selected publication (true/false)
featured = false

# Associated projects
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
projects = []

# Links
url_preprint = "https://eprint.iacr.org/2018/888/"
#url_pdf = "paper.pdf"
url_code = ""
url_dataset = ""
url_project = ""
url_slides = "presentation.pdf"
url_video = ""
url_poster = ""
url_source = ""

# doi
doi="10.1007/978-3-030-25283-0_10"

# Custom links (optional)
# url_custom = [{name = "Custom Link", url = "http://example.org"}]


# Do we use Maths
math = false

# Do we need source code highlighting
highlight = false

# Featured image
#[header]
#image = "headers/bubbles-wide.jpg"
#caption = "My caption

# Tags
tags = []

aliases = [
  '/research/armcluster/',
]
+++

## Software

* [Aarchimate][aarchimate] is a python library that helps write assembly programs by handling the register allocation.
It is a dependency to many of the programs below.
* [AArch64 multipliers][multipliers]: multiplication optimised for Cortex-A53.
* [Microbenchmarking software][microbenchmark]
* [ODROID-C2 management][ansibleplaybooks]: [Ansible][ansible] playbooks for managing a cluster of ODROID C2s.

[aarchimate]: https://github.com/thomwiggers/aarchimate/
[ansible]: https://docs.ansible.com/ansible/
[ansibleplaybooks]: https://github.com/thomwiggers/odroid-playbooks/
[microbenchmark]: https://github.com/thomwiggers/microbenchmark-aarch64/
[multipliers]: https://github.com/thomwiggers/aarch64_multipliers/
