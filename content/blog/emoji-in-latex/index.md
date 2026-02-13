---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "Using Emoji in (pdf)LaTex"
subtitle: "How to use Emoji fonts in LaTeX without resorting to XeLaTeX or LuaLaTeX"
summary: ""
authors: ['thom']
tags: ['latex']
categories: []
date: 2024-04-03T15:04:10+02:00
lastmod: 2024-04-03T15:04:10+02:00
featured: false
draft: false

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
---

I recently wanted to use Emoji in a paper, but I did not want to force my contributors into using LuaLaTeX or XeLaTeX (in which you can just use fancy fonts).
So as a work around, I set up a small helper document that helps me set up emoji as (vector) images instead, which I can then include using `\includegraphics{}`.

To set this up, I create a folder called `emoji` and create the a file called `generator.tex` with the following contents:

```tex
\documentclass[crop]{standalone}

\usepackage{emoji}
\usepackage{fontspec}

\directlua{luaotfload.add_fallback
   ("emojifallback",
    {
        "Apple Color Emoji:mode=harf;",
        "Noto Color Emoji:mode=harf;",
    })}

\setmainfont{Latin Modern Roman}[
  RawFeature={fallback=emojifallback}
]

\begin{document}
\emoji{\theemoji}
\end{document}
```

> [!NOTE]
> Note that this file intentionally won't compile: we'll use a trick to define variable `\theemoji` later.

We also create a `Makefile`:

```Makefile {linenos=table, hl_lines="1 3-5"}
all: mag.pdf fog.pdf prohibited.pdf unicorn.pdf detective.pdf

%.pdf: generator.tex
	lualatex -jobname='$(subst .pdf,,$@)' \
		'\def\theemoji{$(subst .pdf,,$@)}\input{generator.tex}'


.PHONY: clean
clean:
	$(RM) *.aux *-blx.bib *.bbl *.blg *.fdb_latexmk *.fls *.log *.upa *.run.xml

.PHONY: dist-clean
dist-clean: clean
	$(RM) *.pdf
```

Now, if we run `make` in this folder, you should see that the files `mag.pdf`
(:mag:), `fog.pdf` (:fog:), `prohibited.pdf` (🚫), `unicorn.pdf` (:unicorn:),
and `detective.pdf` (:detective:) get created. This is set by the `all` target
on line 1 above: you can add emoji shortcodes to this list and they will
automatically be created. [Refer to the docs for the
emoji package][emoji-doc] for a full list of supported shortcodes.

The magic happens in lines 3-5 of the above listing: we define the variable
`\theemoji` based on the target file name, and use LuaLaTeX's ability to pass
source code directly to the engine to define this variable before including
`generator.tex`.

File `generator.tex` itself is simply a `standalone` class file so that it
automatically crops the document to the size of its contents. We set up the
emoji font using `fontspec`'s more advanced features.

[emoji-doc]: http://mirrors.ctan.org/macros/luatex/latex/emoji/emoji-doc.pdf

Note that this script still requires LuaLaTeX though! We avoid making our
fellow contributors angry by just running the script on their behalf, and we
commit the generated emoji PDF files to our git repository.

Note that you can exempt files from being ignored from git by using exemption
rules in `.gitignore` files as follows:

```gitignore
!*.pdf
```

You can just create a `.gitignore` file in the `emoji` folder to only apply to
that folder.


> [!NOTE]
> Please note that I have not tested this on either Linux or Windows machines
> yet; it likely works on Linux, but Windows might require a different font name
> in `generator.tex`.
>
> Your results will also look different based on what fonts you set.


<!-- vim: set ft=markdown ts=2 sw=2 tw=0 noet :-->
