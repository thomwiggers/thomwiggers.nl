---
layout: default
status: draft
published: true
title: ARM Cluster
author: Thom Wiggers
date: '2017-06-22'
tags:
    - cryptography
    - research
    - ARM
    - AArch64
    - cryptanalysis
    - cluster
    - ECC2K-130
---

# ODROID-C2 Cluster

This page accompanies my Latincrypt 2017 paper *Energy-efficient ARM64 Cluster with Cryptanalytic Applications: 80 cores that do not cost you an ARM and a leg*.
I will upload the paper when it is available.

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

<!-- vim: set wrap : -->
