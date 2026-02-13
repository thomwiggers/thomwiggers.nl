---
title: "Writeup for assignment 3"
date: 2020-03-20
summary: "Solutions and explanations for assignment 3"
draft: true
toc: true
type: "docs"
highlight: true
highlight_languages: ["c", "makefile", "shell", "plaintext"]
authors:
  - me
---

## Exercise 1: Measuring the stack usage.

### Preparation
We write create the following files:

* ``magic_function.h``:

```c

#ifndef MAGIC_FUNCTION_H
#define MAGIC_FUNCTION_H


int magic_function(void);

#endif
```

This headerfile defines the ``magic_function`` to be imported into ``main.c``.
Alternatively, you could use ``extern int magic_function();`` in ``main.c``.

* ``magic_function.c``:

```c

#include "magic_function.h"

#include <stdint.h>
#include <stddef.h>

int magic_function(void) {
    uint8_t space[10000] = {0};

    for (size_t j = 0; j < 10000; j++) {
        space[j] = (char)(j+space[(j+400) % 10000]);
    }
    return space[42];
}
```

This defines the function we're going to be measuring.
We use a bunch of space on the stack and use it in a way that the compiler can't trivially see that the whole computation is pointless.

* ``main.c``


```c
#include <stdio.h>

#include "magic_function.h"

int main(void) {
    // ...
    magic_function();
    // ...
}
```

This is the sample file

* ``Makefile``


```Makefile
CFLAGS = -Wall -Wextra -Wpedantic

main: main.c magic_function.o
    $(CC) $(CFLAGS) -o main main.c magic_function.o

magic_function.o: magic_function.c magic_function.h
	$(CC) -c $(CFLAGS) -o magic_function.o magic_function.c
```

This is a Makefile that will help us test.

### Drawing pictures

We are being asked to measure the amount of stack space ``magic_function()`` uses.
We got the hints to think about what the stack looks like before and after ``magic_function`` is called.

Before we call ``magic_function``, we know the stack looks something like:

```plaintext
+---------------------------+ 0x7ffff...
| program loader            |
+---------------------------+
| main()                    |
+---------------------------+
| UNDEFINED, unused         |
|                           |
+---------------------------+
```

We know that during the call to ``magic_function``, it will look like the following:


```plaintext
+---------------------------+ 0x7ffff...
| program loader            |
+---------------------------+
| main()                    |
+---------------------------+
| magic_function()          |
|  uint8_t space[1000] = {  |
|    0, 1, 2, ...}          |
+---------------------------+
```

The question is then what happens after we return from ``magic_function``: the stack pointer will be decreased, but what happens to the stuff on the stack?

```plaintext
+---------------------------+ 0x7ffff...
| program loader            |
+---------------------------+
| main()                    |
+---------------------------+
| UNUSED: left behind       |
|  uint8_t space[1000] = {  |
|    0, 1, 2, ...}          |
+---------------------------+
```

### The plan

Before we call ``magic_function``, we will make sure the stack looks like:

```plaintext
+---------------------------+ 0x7ffff...
| program loader            |
+---------------------------+
| main()                    |
+---------------------------+
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 ....  |
+---------------------------+
```

We can do this by either just writing out of bounds, or by creating a different function that allocates some space on the stack.

We can put the following snippet of code before the ``magic_function()`` call:

```c
for (int j = 4; j < 4194304; j++) {
    *((char*)&j-4) = 0x41;
}
magic_function();
```

Now, after ``magic_function`` returns, we expect the stack to look like:
```plaintext
+---------------------------+ 0x7ffff...
| program loader            |
+---------------------------+
| main()                    |
+---------------------------+
| 0x00 0x01 0x02 ...  ...   |
| ...space [3..1000] ...    |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 0x41  |
| 0x41 0x41 0x41 0x41 ....  |
+---------------------------+
```

So we can simply start counting until we start seeing a sequence of ``0x41s`` again.
We're careful to check if we see more than just one, because ``magic_function`` probably writes at least one ``0x41`` byte.

```c
int num_flags_seen = 0;
int j;
for (j = 4; j < 4194304 && num_flags_seen < 10; j++) {
    if (*((char*)&j-j) != 0x41) {
        num_flags_seen = 0;
    } else {
        num_flags_seen++;
    }
}

printf("magic_function took %d bytes", j-10);
```

## Exercise 2: malloc search

We need to write a program that determines the maximum amount of heap space that we can allocate.
We will use a binary search style approach for figuring out how much we can allocate.
When we can allocate a certain size of memory, we know that we will get a pointer back, if we can't we'll get ``NULL``.
We make sure to ``free()`` any valid pointers that we obtain.

```c
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

int main(void) {

    size_t min = 1, step = SIZE_MAX-1;

    while (step > 0) {
        printf("Current minimum = %zu, step = %zu\n", min, step);
        void *ptr = malloc(min+step);
        if (ptr != NULL) {
            min += step;
            free(ptr);
        } else {
            step /= 2;
        }
    }
    printf("Maximum size that can be allocated: %zu\n", min);
}
```

We obtain that the maximum size that can be allocated is about 23 GiB on my laptop.

### b) does this number change.

On my laptop, it does not. The kernel overcommits memory: it assumes that until I use it all it can get away with giving me more than the system actually supports.

### c) What about ``calloc``

It turns out that I **get the same result**, unlike what we expected. (libc and compiler versions: glibc 2.32, gcc 10.1.0).
This means that the slides I inherited are no longer correct — ``calloc`` does not guarantee that the physical memory is there, it only initialises it to zero.

What's probably happening is that the operating system maps all of the pages of virtual memory obtained by our ``calloc`` calls map onto the "zero page"; a special page that the OS makes sure is always empty.
Only when we will write to the page, will the OS copy the zero page to physical memory and process the write (Copy on Write).
This makes the entire procedure much more efficient.

## Exercise 3: address maths

The only special case is c: there &x obtains a pointer of type (``int32_t[4]*``).
That means that the ``+1`` will add ``sizeof(int32_t[4])``.

## Exercise 4: matrix multiplication

This program leaks memory all over the place and will soon crash when it runs out of memory.

When allocating `m` and `mt`, it allocates space for 1000 pointers to ``unsigned long long``s.
In the ``for`` loops, it then allocates space for each of the ``unsigned long long`` values.
At the end of the program, it only frees ``m`` and ``mt``, not the 2000 ``unsigned long long`` values!

We can fix the code by adding this ``for`` loop:

```c
for (i = 0; i < 1000; i++) {
    free(m[i]);
    free(mt[i]);
}
```

In addition, this program never checks if ``malloc`` returns ``NULL``. We could fix this by adding a wrapper around ``malloc``:

```c
void* malloc_safe(size_t size) {
    void *ptr = malloc(size);
    if (ptr == NULL) {
        puts("MALLOC FAILED");
        exit(1);
    }
    return ptr;
}
```

We can then replace all of the ``malloc`` calls by this function.


## Exercise 5: messing with strings

We were given the following program (filled in some student numbers):

```c
int main(void) {
    char *s1 = malloc(9);
    if (s1 == NULL) return 1;
    char *s2 = malloc(9);
    if (s2 == NULL) return 1;
    strcpy(s1, "s0123456");
    strcpy(s2, "s3456789");
    // do your attack
    printf("student 1: %s\n", s1);
    printf("student 2: %s\n", s2);
    return 0;
}
```

### Why strcpy?

If we would write ``s1 = "s01234567"``, ``s1`` would be assigned the pointer to the ``code`` segment of the program where the constant value ``"s01234567"`` lives, instead of putting the value in the heap-allocated memory.

### Why 9 bytes?

The ``NULL`` byte also needs some space.

### Concatenating these two values

If we assume that `s1` is allocated before `s2`, we can do the following:
we simply replace all `0x00` bytes between ``s1`` and ``s2`` by spaces (``0x20``).

```c
char *myptr = s1;
while (myptr < s2) { // <- comparing pointers is strictly speaking undefined behaviour
    if (*myptr == 0x00) {
        *myptr = ' ';
    }
    myptr++;
}
```

### A harder version

In the original version of this exercise, you needed to do it without using the addresses of ``s1``, ``s2``.

We would use the fact that ``malloc`` will likely give us memory that is close to ``s1`` and ``s2`` and then search for ``s1`` and ``s2``.

```c
char *heaploc = malloc(1);
char *s1loc = 0, *s2loc = 0;
for (int offset = -100; offset < 100 && (s1loc == 0 || s2loc == 0); offset++) {
    if (0 == memcmp(heaploc+offset, "s0123456", 9)) { // compare with known value of s1
        printf("Found s1");
        s1loc = heaploc+offset;
    }
    if (0 == memcmp(heaploc+offset, "s3456789", 9)) { // compare with known value of s2
        printf("Found s2");
        s2loc = heaploc+offset;
    }
}
char *myptr = s1loc;
while (myptr < s2loc) {
	if (*myptr == 0x00) {
		*myptr = ' ';
	}
    myptr++;
}
```
