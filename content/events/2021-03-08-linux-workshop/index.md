---
title: Thalia's Linux Workshop 2021
event_url: https://thalia.nu/events/723/
location: virtual
address:
  street: null
  city: null
  region: null
  postcode: null
  country: null
summary: |
  Workshop on getting around on the command line.
  As a good prep for the course Hacking in C, I will show you how to get around on the command line, how to manage your files and how to run programs.
abstract: null
date: 2021-02-26T14:37:31+01:00
authors:
  - me
tags:
  - teaching
  - hacking in c
featured: false
image:
  caption: ""
  focal_point: ""
  preview_only: false
links:
  - type: slides
    url: tutorial.pdf
  - type: video
    url: https://youtu.be/nkFrGK-HnoQ
slides: ""
projects: []
event_start: 2021-03-08T12:45:00+01:00
event_end: 2021-03-08T13:15:00+01:00
event_all_day: false
event_name: Studievereniging Thalia Lunch Talk
---


Do you associate black screens with green text on them with the "hacker known as 4chan"? Is the first thing you do when the lab computer booted Linux rebooting the PC to your Windows safe space? Do you panic whenever you see ``cmd.exe``? And are you taking Hacking in C soon?

Then this command line boot camp is probably a good idea. As a good prep for the course Hacking in C, I will show you how to get around on the command line, how to manage your files and how to run programs.

This workshop is aimed at first-year students who have never really touched any command line before. It is recommended, but not required, for Hacking in C. If you have done any intermediate-level stuff in Windows .bat files, or know what `cd` and `ls` are, you are possibly already overqualified. If you know how `grep`, `find` and/or pipes work, you are definitely overqualified.

## Required preparation

You will need to have access to Linux of whatever flavour to participate in this tutorial.
The flavour of Linux does not matter: if you've already got access to a Linux box that's enough.

You can participate in the Workshop if you can log in to [``lilo.science.ru.nl`` over SSH][lilo-ssh].
You will need a Science faculty account — you can't log in on ``lilo`` via your s-number.
Alternatively you can set up a Linux virtual machine — this is also helpful for Hacking in C.

[lilo-ssh]: https://wiki.cncz.science.ru.nl/Hardware_servers#Linux_.5Bloginservers.5D.5Blogin_servers.5D

We suggest installing Ubuntu 20.04 on VirtualBox.
You can consider following [this tutorial](https://fossbytes.com/how-to-install-ubuntu-20-04-lts-virtualbox-windows-mac-linux/).

### A note on Linux subsystem for Windows

Linux subsystem for Windows is enough Linux for most purposes and will work for this workshop.
However, it **will not** be sufficient for Hacking in C: due to differences in the memory manager to "real Linux" we typically run into issues in the homework assignments.


## Other resources

* [last year's video](https://youtu.be/I1N4T0UXuaA) where we went a bit further than during this year's (shorter) workshop.
* [MIT's Missing Semester](https://missing.csail.mit.edu/2020/course-shell/)
* [Cheat sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
* [Bash scripting cheat sheet](https://devhints.io/bash)
* [The Linux Command Line (free book)](http://linuxcommand.org/tlcl.php)
* [Extensive shell scripting tutorial](https://www.shellscript.sh/)
