---
layout: post
status: publish
published: true
title: Time-invariant equality in assembly
author: Thom Wiggers
author_login: Thom Wiggers
author_url: http://thomwiggers.nl
date: '2014-03-21 18:25:10 +0100'
date_gmt: '2014-03-21 17:25:10 +0100'
categories:
- security
tags:
  - assembly
  - cryptography
  - software
  - avr
comments: []
highlight: true
highlight_languages:
  - avrasm
---

<p>For crypto code it's important that it's time-invariant, otherwise it is
vulnerable to timing attacks. I've had to build this time-invariant equality
test from scratch, because I couldn't find something on Google. I hope it's
useful to someone else. </p>

<!--more-->

```avrasm
;
; Linear time equality
;
; Author: Thom Wiggers
;

; based on this C code:

; int equals (int a, int b) {
;   unsigned long long t = a ^ b;
;   return 1-((-t) >> 63);
; }

; stores result in first argument
.macro linear_equals ; register A, register B
EOR @0, @1
NEG @0
BRVS skiplinearequalsoverflow ; I don't know how else to take care of the overflow.
  ROR @0 ; if this is just one operation, it still is time-invariant.
skiplinearequalsoverflow:
LSR @0
LSR @0
LSR @0
LSR @0
LSR @0
LSR @0
LSR @0
NEG @0
inc @0
.endm


.exit
;; everything here isn't executed
;; This test proves that the above code works.
TEST:
mov r2, r16
mov r3, r17
linear_equals r2, r3
BREQ skipnop
  CP r16, r17 ; check if it's indeed equal
  BREQ skipnop
  nop ; for breakpoints
  inc r15 ; amount of mistakes
skipnop:
inc r16
CPI r16, 0xFF
BRNE skipinc ; j + 1, i = 0
  inc r17
  clr r16
skipinc:
CPI r17, 0xFF
BRNE skipbreak ; done
  break
skipbreak:
rjmp test
```
