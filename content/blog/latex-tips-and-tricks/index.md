---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "LaTeX Tips and Tricks"
subtitle: ""
summary: ""
authors: ['thom']
tags: ['latex', 'technology']
categories: []
date: 2022-05-11T15:46:21+02:00
lastmod: 2023-08-16T10:30:00+02:00
featured: false
draft: false

highlight: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Some LaTeX package imports."
  focal_point: "TopLeft"
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

After a [discussion on twitter](https://twitter.com/ThomWiggers/status/1524123550378037249) I decided I should write down a few of the tips and tricks I've learnt over the years of writing papers and many other things in LaTeX.

## Pandoc

If you're very sure you need a full-blown LaTeX document, continue reading below.
Otherwise, triple and quadruple-check if you can't just get away with writing Markdown and just use `pandoc` to convert your document to LaTeX/PDF.

[The Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template) seems particularly cool.

## Editor

I like Visual Studio Code for LaTeX nowadays.
I use the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin.
It's worth going through the settings if you have e.g. `subfiles` in your project or need to tweak the builds.

## Compiling

Compiling TeX is a pain.
You commonly see people using Makefiles with the "usual" invocation of `pdflatex`:

```makefile
main.pdf: main.tex *.tex *.bib
	pdflatex main
	bibtex   main
	pdflatex main
	pdflatex main
```

But this invocation takes so much time!
Especially if your page layout hasn't changed (so references haven't moved), then it mostly runs those extra runs unnecessarily.

A smarter way is using [Latexmk](https://www.ctan.org/pkg/latexmk/) which just runs the compiler and BibTex automatically, how many times is necessary.

## Check out the KOMA document classes

If you're not stuck to a publisher template, check out the `KOMA-Script` document classes.
Basically use `scrartcl` instead of `article`, or `scrreport` instead of `report`, or `scrbook` instead of `book`.
They're probably part of your TeX distribution and you might like the results.
Minor issue: the English documentation has _most_ things, but some things are only documented in German.

## Split up your projects

Use `\input` to separate your different files, e.g. by section:

```latex
% these automatically get .tex appended
\input{introduction}
\input{preliminaries}
\input{chapter3}
% ...
```

If you're writing very large sections/chapters that take a while to compile, look into `subfiles` (mentioned below).

## Useful packages

I generally use the following stuff in my preamble:

```latex
% It's 2022. UTF-8 input for TeX. 
% Should be one of the first things to import.
\usepackage[utf8]{inputenc}

% Language support for hyphenation etc. 
% Always import if you're not writing Murican.
% If you are writing American English, probably still doesn't hurt.
\usepackage[british]{babel}

% Todo notes. Useful when collaborating with people.
% I like to add some newcommands as well:
%  \newcommand{\todothom}[1]{\todo{Thom: #1}}
%  \newcommand{\todothominline}[1]{\todo[inline]{Thom: #1}}
% Because margins are small and I have good eyes: small notes.
\usepackage[textsize=scriptsize]{todonotes}

% does something to make quotes make sense.
\usepackage{csquotes}

% Fancier font features. Imports hyperref.
\usepackage{microtype}

% Fancier font than the regular computer modern.
% Caveat emptor: fonts are often a publisher template thing,
% you should probably check if your venue is actually okay with this.
\usepackage{lmodern}

% I believe this encodes fonts into your PDF.
% Best imported after fonts.
\usepackage[T1]{fontenc}

% Murder widows and cubs hard. Might mess with your page limit.
\usepackage[all]{nowidow}
```

This package just makes dealing with commands so much easier:
`\newcommand{\foo}{some text\xspace}` makes `\foo` not eat the space
(and `\foo.` still works like it should!).
But there are
[some](https://tex.stackexchange.com/a/86620/9454)
[concerns](https://tex.stackexchange.com/q/180686/9454)
that it sometimes fails, and it's hard to predict when it will, which is a bad thing™️.
I still use it.

```latex
% This package just makes dealing with commands so much easier:
% \newcommand{\foo}{some text\xspace} makes \foo not eat the
% space (and \foo. still works like it should!).
% Caveat emptor:
%  * https://tex.stackexchange.com/a/86620/9454
%  * https://tex.stackexchange.com/q/180686/9454
\usepackage{xspace}
```

## Including code

I like the `minted` package for code.
It does have a bit more setup: you need to run your TeX compiler with `-shell-escape`.
You also need `pygments` on your computer.

[Overleaf has a nice tutorial](https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted).

## In-document references
The `cleveref` package makes referencing this a lot easier.

```latex
% Fancy automatic references
\usepackage[nameinlink]{cleveref}
% Make sure you import this *after* hyperref (or it will complain)
```

With these options, you can write the following:

```latex
We already talked about X in \cref{sec:someother}.
```

And this will turn `\cref{sec:someother}` into a linked `section 42` automatically.
If you start a sentence with your reference, use the capitalised `\Cref` variant.
There's a whole bunch of styles.

## Bibliography

### Using a bibliography collection

You can maintain your bibliographies yourself, but I like using [cryptobib](https://cryptobib.di.ens.fr).
It has most cryptography papers in it and the style is fairly consistent.
A big downside is that it will usually link to the paywalled version of a paper.
Also, it's over 20 megabytes of data that `bibtex` will need to process.
If you use `biber` (because you like `biblatex`), this can even push your build time to over a minute.
However, most publishers will only accept BibTex anyway (publishers are why we can't have nice things).

### Using BibLaTeX

In my thesis template, I included the following:
```latex
\usepackage[backend=bibtex,backref=true]{biblatex}
```

Using `bibtex` doesn't allow me to use all of `biblatex`'s fanciness.
However, `backref` is already pretty nice and once my thesis is more finalised, I will probably switch to `biber` for the final runs.
By then I will probably have extracted what I want from Cryptobib, to tweak the references into their final forms.

If you want to go into more experimental territories, I have [a hacky script](https://github.com/thomwiggers/extract_from_bibliography) that can extract references from large bibliographies.
You will need to mess with your build chain.

## Pretty hyperlinks

The `hyperref` package takes some options to make the URLs a lot prettier.
We use `hypersetup` here to pass the config.

```latex
\usepackage{xcolor}
\hypersetup{
    breaklinks=true,
    colorlinks=true,
    linkcolor=[rgb]{0.65,0,0},
    urlcolor=[rgb]{0,0,0.65},
    citecolor=[rgb]{0,0.65,0}
}
```

## Pretty tables

Use `booktabs` and **never use vertical lines**.
If you need to separate two columns for organisation purposes, try if you can't just do it by adding extra spacing: you can add `@{\hskip 20pt}` in your column specification.

```latex
\usepackage{booktabs}
% ...
\begin{tabular}{lr}
  \toprule
  \bf foo & \bf bar \\
  \midrule
  baz & 1 \\
  \bottomrule
\end{tabular}
```

### Aligning text in (title) rows differently
I like to make the title row bold font.
If there's a column that's, for example, right-aligned (`r`), then I sometimes want to change the alignment just for the title row.
You can do that by using `\multicolumn{1}{l}{your column content}`: you define a 1-column multicolumn cell and you can specify how you want that cell aligned.

### Filling in tables from measurements

I have measurement scripts in my research a lot, for example for benchmarks.
I like to process those benchmarks with a simple python script that generates LaTeX files for me that just define `\newcommand`s for each result:

```latex
% X25519_RSA2048_RSA2048_clauth_RSA2048_RSA2048_30.947ms_0_1000mbit.csv
\newcommand{\resfastsigcacheERauthRRencrypting}{68.8}
\newcommand{\resfastsigcacheERauthRRclientdone}{68.8}
\newcommand{\resfastsigcacheERauthRRserverdone}{38.2}
\newcommand{\resfastsigcacheERauthRRserverexplicitauthed}{66.0}
% ...
```

These follow a set pattern, becuase I then like to define my table rows as follows:
I define a `\newcommand` that lays out a single table row for me:
```latex
\newcommand{\experimentcached}[2]{
    & % after section title
    #1 & % experiment name
    \csuse{resfast#2encrypting}  &
    \csuse{resfast#2clientgotreply} &
    \textbf{\csuse{resfast#2serverexplicitauthed}} &
    \csuse{resfast#2serverdone} &
    % slow
    \csuse{resslow#2encrypting} &
    \csuse{resslow#2clientgotreply} &
    \textbf{\csuse{resslow#2serverexplicitauthed}} &
    \csuse{resslow#2serverdone} \\
}
```
And then I use this macro to fill in my table:
```latex
% table headings, bla...
\experimentcached{TLS~1.3}{sigcacheERauthRR}
\experimentcached{SIKE-c}{sigcacheScFauthFF}
\experimentcached{MLWE/MSIS}{sigcacheKDauthDD}
\experimentcached{NTRU}{sigcacheNFauthFF}
% ... table footer
```

The magic here is in `\csuse` (from `etoolbox`), which allows me to fetch the defined `\newcommand` macros with the results from the `\experimentcached` macro parameter.

## Finding overfull hboxes

Horizontal boxes that are overfull are a common thing that you will run into.
At first this warning doesn't make sense, but what LaTeX is trying to tell you is that it needs too much horizontal space and thus is spilling over into your margins.

The following command helps you locate where this is happening.
Many packages set this automatically if you enable `draft` mode.
However, `draft` mode generally disables included pictures, which is super annoying.

```latex
% highlight overfull boxes with a thick line
\overfullrule=10mm
```

If you have a paragraph that is spilling (usually because of a word/macro TeX can't hyphenate),
you should try to either reword that paragraph or add in manual hyphenations.
Note that if a word is already hyphenated, LaTeX will not add additional hypenations.
For example, `extraordinarily-long` would only break between `extraordinarily` and `long`.
With the `hyphenat` package, you can write `extraordinarily\hyp{}long`, and then LaTeX will allow it to break in `extraordinarily` as well (because I don't think `long` can be hyphenated).

If you get this error in paragraphs/sections that you don't have control over, like the bibliography, or if you don't care so much to reword, you can also try slapping the paragraph between `\sloppy` and `\fussy`. These two commands allow LaTeX to mess with spacing in ways that are often considered ugly but are probably better than poking into the margin.

```latex
\sloppy
\bibliographystyle{splncs04}
\bibliography{cite,cryptobib/abbrev3,cryptobib/crypto}
\fussy
```

## Different versions of your paper (long/short, anonymous)

If you're hitting a page limit, you often need to omit stuff that you want to include in an "online" version.
You might also need an anonymous version of your paper.
The way I've generally done this is by using plain TeX `if` statements:

```tex
\newif\iffullversion
\fullversionfalse
% \fullversiontrue
```

This is not the prettiest way of doing conditionals, but it's very easy and works almost anywhere, including in titles or author listings.

You would use it as follows:

```latex
\iffullversion
This text was cut from the submitted version: page limits suck.
\else
See the full version at website for this paragraph.
\fi
```

## More advanced hints

### A hacked LNCS template

If you're using `llncs`, you might want to take a peek at [this hacked `llncs` template](https://github.com/latextemplates/LNCS), which makes a bunch of improvements that may or may not be okay with Springer.

### Fixing the PDF bookmarks in ``llncs.cls``

`llncs` sets the table of contents depth to 0, to make sure you don't print it.
But this change also breaks PDF bookmarks, so make sure to add the following option to your `hyperref` setup:

```latex
% on package load:
\usepackage{bookmarksdepth=2}{hyperref}

% or using hypersetup
\hypersetup{bookmarksdepth=2}
```

### Other LaTeX compilers

If you want to use fancier fonts, and you don't care about a publisher: `LuaLaTeX` is probably the way to go right now.

### Standalone TeX graphics

If you find your TikZ graphics are increasing your compile times, look into [`standalone`](https://www.ctan.org/pkg/standalone).
This package can even compile your pictures for you and just include the `pdf` directly after the first build, automatically!

### Compiling sections independently

The [`subfiles` package](https://www.ctan.org/pkg/subfiles) is super useful if you have book-sized documents.
It allows you to compile e.g. chapters independently.
See [this tutorial](https://jonasdevlieghere.com/modular-latex-with-subfiles/)

### Advanced typography warnings

See the [`inpnattypo` package](https://www.ctan.org/pkg/impnattypo).
Warning: the authors are _French_ pedantics.

```latex
% Fancy typography issues
% https://www.ctan.org/pkg/impnattypo
\usepackage[hyphenation,parindent,
            lastparline,nosingleletter,
            homeoarchy,rivers]{impnattypo}
```

## Don't use

The following are bad, in my opinion:

### Narrow margins (e.g. `a4wide`)
The margins in LaTeX document classes are set in such a way that they make the text easy to read.
If you increase the line length a lot (ie. smaller margins), your text just turns into a hard-to-get-into wall.
If you're not trying to save actual trees (ie. you're printing the document), it doesn't matter!
You may want to try `scrartcl` if you're printing on A4, though.
