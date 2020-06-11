+++
title = "Assignments"
date = 2020-03-20
summary = "Assignments for HiC"

draft = false
toc = true
type = "docs"

highlight = true
highlight_languages = ["c", "makefile", "shell", "plaintext"]

authors= [
  "thom",
]

[menu.hic2020]
  name = "Assignments"
  parent = "Hacking in C"

weight = 30
+++


## Assignment 1

* **Download:** [Assignment 1](assignment1.pdf)
* **Deadline:** April 21, **12:30**.
* **Hand-in:** [Brightspace][]

### Extra resources

* [(YouTube) Writing your first shell script](https://www.youtube.com/watch?v=eiBVlxxu3so)
* [Documentation for different printf() types](https://icecube.wisc.edu/~dglo/c_class/printf.html)
* [`man man` (how to use the manual command)](https://manpage.me/index.cgi?apropos=0&q=man&sektion=0&manpath=Debian+8.1.0&arch=default&format=html)

## Assignment 2

* **Download:** [Assignment 2](assignment2.pdf)
* **Deadline:** May 12, **12:30**.
* **Hand-in:** [Brightspace][]

### Extra resources

* [C - Data Types](https://www.tutorialspoint.com/cprogramming/c_data_types.htm)
* [Pointers](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/a-pointer-is-a-variable)
* [More on pointers](https://www.cs.yale.edu/homes/aspnes/pinewiki/C(2f)Pointers.html)
* [Calculating next memory address](https://denniskubes.com/2012/08/17/basics-of-memory-addresses-in-c/)
* [Underestainding memory address in C](https://computer.howstuffworks.com/c23.htm)
* [IBM inttypes.h](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.bpxbd00/inttyph.htm)
* [One's and two's complement calculator](https://ncalculators.com/digital-computation/1s-2s-complement-calculator.htm)
* [Binary <-> decimal converter](https://www.rapidtables.com/convert/number/binary-to-decimal.html)
* [One's complement](https://www.tutorialspoint.com/one-s-complement)
* [Two's complement](https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html)
* [Writing out binary numbers](https://stackoverflow.com/questions/6373093/how-to-print-binary-number-via-printf)

## Assignment 3

* **Download:** [Assignment 3](assignment3.pdf)
* **Deadline:** May 19, **12:30**.
* **Hand-in:** [Brightspace][]
* **Writeup:** [Writeup](writeup-ass3/)

### Extra resources

* [``man malloc``](http://man7.org/linux/man-pages/man3/malloc.3.html)
* [An annotated example of local variables on the stack](https://www.cs.rutgers.edu/~pxk/419/notes/frames.html)

#### Initializing an array with a fixed value

The below code will initialize the whole of ``array`` with the value ``0``.
```c
unsigned char array[SIZE] = {0};
```

**Unfortunately**, I was mistaken, and this only works for zero!
Setting other values will only set that value for the first element and the rest will still be zero.

If you want to set a value on the whole array, try using ``memset``:
```c
memset(array, 0, SIZE);
```

## Assignment 4

* **Download:** [Assignment 4](assignment4.pdf)
* **Deadline:** May 26, **12:30**.
* **Hand-in:** [Brightspace][]
* **Writeup:** [Writeup](writeup-ass4/)

### Extra resources

#### Thom's hacking utilities

These scripts can help you do some menial stuff, like printing addresses in little-endian order, as demonstrated in the lecture.
Follow the instructions in the ``README.md`` to install them.

 * [Thom's hacking utilities](utilities.tar.gz)

## Assignment 5

* **Writeup:** [Writeup](writeup-ass5/)

The last homework assignment will be a bit different from the previous ones. I have spent the last weeks creating a website to host "capture the flag" style hacking challenges, which is where I will run the graded challenges on. I demoed it a little bit in the lecture.

This week we traditionally have the remote buffer overflow challenge, which more or less asks of you to do the same thing as I did in the lecture. You can submit your write-up through the site as well.

Sign up at https://hackme.rded.nl. You will need to fill in your student number and you can only sign up once. Please terminate your running processes after you're done with them. This weeks homework is completing the two challenges that are posted there.

### Extra resources

* [ASCII/Hex encoder / Decoder](https://www.convertstring.com/EncodeDecode/HexDecode). This encoder doesn't chocke on null bytes or weird characters. Note that it doesn't like ``0x`` in its input.
* Classic tutorial on buffer overflows. Note that it is a bit outdated, because it's from way before AMD64 (1996). [Smashing the stack for fun and profit](https://insecure.org/stf/smashstack.html)

[Brightspace]: https://brightspace.ru.nl/d2l/home/88557
