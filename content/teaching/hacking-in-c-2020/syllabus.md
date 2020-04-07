+++
title = "Syllabus Hacking in C 2020"
date = 2020-04-07
summary = "The course outline"

draft = false
toc = true
type = "docs"

highlight = false

authors= [
  "thom",
]

[menu.hic2020]
  name = "Syllabus"
  weight = 1
  parent = "Hacking in C"
+++
---
# Syllabus Hacking in C 2020

| Version | Changes         |
|---------|-----------------|
| 07-04   | Initial version |

## TL;DR

* **Course:** NWI-IPC025 Hacking in C
* **Credits:** 3 EC
* **Schedule**: Fourth Quarter of 2019--2020
    * **Start:** 13 April 2020
    * **Exam date:** 24 June 2020 (for now)
* **Main lecturer:** Thom Wiggers <thom@thomwiggers.nl>
* **Supporting lecturers:** Denisa Greconici <D.Greconici@cs.ru.nl>
* **Course URLs (clickable):**
    * [Discord][] (tutorials)
    * [Brightspace][] (handing in assignments)
    * [Course Website][] (supplemental resources, slides)
    * [Lectures][thom on youtube] (live streams and recordings)
    * [OSIRIS][] ("official" but outdated syllabus)

## Preliminary Schedule

| When | What     | Subject                     | Deadline    |
|------|----------|-----------------------------|-------------|
| 13-4 | ~~Lecture~~  | Easter Monday           |             |
| 14-4 | Tutorial | C programming, Shell, Make  | 21-4 12:30 |
| 20-4 | Lecture  | Hello, C, pointers, alignment |          |
| 21-4 | Tutorial | C programming, Shell, Make  | 12-5 12:30 |
| 04-5 | Lecture  | Hello, C, pointers, alignment |          |
| 05-5 | ~~Tutorial~~ | Liberation Day |    |
| 11-5 | Lecture  | Attacks 1: printf, buffers  |             |
| 12-5 | Tutorial | Stack, Heap, printf         | 19-5 12:30  |
| 18-5 | Lecture  | Attacks 2: overflowing the return address |             |
| 19-5 | Tutorial | More attacks                | 26-5 12:30  |
| 25-5 | Lecture  | Attacks 3: ROP, ASLR        |             |
| 26-5 | Tutorial | Attacks, cont.              | 2-6 12:30   |
| 01-6 | ~~Lecture~~ | Pentecost Monday         |             |
| 02-6 | Tutorial | Attacks, wrapup             |   8-6 12:30 |
| 08-6 | Lecture  | Safety (probably not in exam) |   |
| 09-6 | Tutorial | Introduction Exam?          | 24-6 12:30 ?|

## Course website

Thom hosts the [Course Website][] and will try to fill this space with supplemental resources and links.
There already is a [Makefile tutorial][] and a [Shell tutorial][] on that website.
We will also put slides with the links to the lectures on those pages.

### Call for Contributions

There are a quadrillion resources on the internet that could replace or supplement any part of this course.
I would like to invite anyone to contribute to the course website.
It is [hosted on GitHub][course website on github] and there are _Edit_ links below pages.
Contributions will be reviewed by Thom via the GitHub pull request system.

## Lectures

Lectures will be done at the scheduled time on Mondays, 10:45.
We will follow the 'regular' concept of lectures, including the scheduled break.
They will be live-streamed on YouTube and we will be able to interact via chat.
Although recordings will be made available, it would be appreciated if you are present for the lectures.

**The first lecture.**
As the first lecture is scheduled for Easter Monday, there will be no regular lecture that week.
Instead, we will provide some videos and other materials for you to get started with Linux and C programming.
This means that the tutorial will continue as scheduled!

## Tutorials

Tutorials will happen on Discord instead of in a computer lab.
You will need to install a Linux on your computer.
We recommend installing Ubuntu 19.10 in a virtual machine.
Any flavour of Linux should be sufficient, however.

Please note that Linux Subsystem for Windows is *not* sufficient.
That version of Linux isn't really Linux because Windows still provides the operating system features through a Linux-like API.
As a consequence, the types of attacks that we will be doing might not work reliably or at all.

## Homework

Homework will be handed in and graded by the student assistants.
In principle, the deadline is a week after the tutorial, _after_ the second tutorial, but due to holidays this is sometimes longer.
You will need to hand in **all** homework to be able to participate in the exam.

### Grading
Grades given will be the familiar "Good/Sufficient/Insufficient" system.
If you don't hand in any real work, you might also receive a **Fail** mark.
In this case, you should **contact the student assistant** as soon as possible and discuss how to amend this.

### I couldn't figure out an assignment
If you can't figure out how a particular assignment works, please still try to hand in something the SAs can give feedback on.
For example, consider writing about the following things:

* What did you try?
* What problems did you run into?
* How much worked of what you tried?
* Why do you think that (did not) work?

## Exam

You need to have participated in the homework to take the exam.

**The following is not final yet**

We will probably be doing some assignments instead of the normally scheduled, written exam, if we have to do it online.
You will complete these individually and write a short report on what you did.
We have also not decided yet on how much time you will have to complete this.

### Learning goals (copy/paste from [OSIRIS][])

* explain how standard C data types are represented, and write C programs to inspect and manipulate these representations
* explain how the stack and heap are used to allocate data in C programs
* write C programs that makes use of pointers and pointer arithmetic
* explain how the stack is used to administer procedure calls
* explain how buffer overflows work
* explain some of the countermeasures against these vulnerabilities, how these work, and apply some of them
* develop simple exploits for code with buffer overflow weaknesses.

[Discord]: https://discord.gg/E7ZRazd
[Brightspace]: https://brightspace.ru.nl/d2l/home/88557
[Course Website]: https://thomwiggers.nl/teaching/hacking-in-c-2020/
[thom on youtube]: https://www.youtube.com/channel/UCwwbVGvvWeGDUuCRuTHaENQ/
[OSIRIS]: https://www.youtube.com/channel/UCwwbVGvvWeGDUuCRuTHaENQ/
[Makefile tutorial]: https://thomwiggers.nl/teaching/hacking-in-c-2020/makefiles/
[Shell tutorial]: https://thomwiggers.nl/teaching/hacking-in-c-2020/shell-tutorial/
[course website on github]: https://github.com/thomwiggers/thomwiggers.nl/tree/new-site/content/teaching/hacking-in-c-2020
