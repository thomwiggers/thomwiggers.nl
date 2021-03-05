---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Thalia's Linux Workshop"
event: Studievereniging Thalia Lunch Talk
event_url: https://thalia.nu/events/723/
location: virtual
address:
  street:
  city:
  region:
  postcode:
  country:
summary: |
  Introduction to some basic Linux concepts.
abstract:

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-03-08T12:45:00+01:00
date_end: 2021-03-08T13:15:00+01:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2021-02-26T14:37:31+01:00

authors: ['thom']
tags: ['teaching', 'hacking in c']

# Is this a featured event? (true/false)
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

# Optional filename of your slides within your event's folder or a URL.
url_slides: tutorial.pdf

url_code:
url_pdf:
url_video: https://youtu.be/nkFrGK-HnoQ

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---


See also [last year's video](https://youtu.be/I1N4T0UXuaA) where we went a bit further than during this workshop.


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

* [MIT's Missing Semester](https://missing.csail.mit.edu/2020/course-shell/)
* [Cheat sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
* [Bash scripting cheat sheet](https://devhints.io/bash)
* [The Linux Command Line (free book)](http://linuxcommand.org/tlcl.php)
* [Extensive shell scripting tutorial](https://www.shellscript.sh/)
