---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Extract only needed citations from large bibfiles"
subtitle: ""
summary: ""
authors: ['thom']
tags: ['software', 'research']
categories: ['software', 'open source']
date: 2019-09-18T15:03:11+02:00
lastmod: 2019-09-18T15:03:11+02:00
featured: false
draft: false

math: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

highlight:
highlight_languages:
  - Makefile
---

I like to use [cryptobib][cryptobib], because it gives me consistent results and it contains almost everything relevant to me.

However, as ``crypto.bib`` is over 725000 lines long, parsing it to create the bibliography takes a long time.
This means that my $\LaTeX$ compile jobs take much too long.

I have now written a python script that will allow you to extract entries from large bibliographies.

This script will take your biblatex ``.bcf`` file and then extract the needed entries from larger bibfiles.


## Makefile example
The only thing is that you need make sure to run the script if you add new references to your document.
You can do this manually, or use the below example ``Makefile`` to keep your extracted ``.bib`` file up to date.

```Makefile
.PHONY: main.pdf
main.pdf: extracted_cryptobib.bib
	./latexrun --bibtex-cmd=biber -Wall main.tex
	# or latexmk, or just pdflatex a bunch of times...

latex.out/main.bcf:
	mkdir -p latex.out
	pdflatex -interaction=batchmode -output-directory=latex.out main

extracted_cryptobib.bib: latex.out/main.bcf cryptobib/crypto.bib
	python3 extract_from_bibliography.py $^ > $@
```

You can find this script [on it's GitHub page][projecturl]

[cryptobib]: https://cryptobib.di.ens.fr
[projecturl]: https://github.com/thomwiggers/extract_from_bibliography/
