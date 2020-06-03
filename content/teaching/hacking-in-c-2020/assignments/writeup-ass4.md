+++
title = "Writeup for assignment 4"
date = 2020-06-03
summary = "Solutions and explanations for assignment 4"

draft = true
toc = true
type = "docs"

highlight = true
highlight_languages = ["c", "makefile", "shell", "plaintext"]

authors= [
  "denisa",
]

[menu.hic2020]
  name = "Writeup Assignment 4"
  parent = "Assignments"

#weight = 30
+++

## Exercise 1: Simple buffer overflow. Overwrite string
For this exercise we have to give an input to the program such that it executes `/bin/sh` instead of `/bin/ls`. By looking at the code we observe the following:
* `strcpy(buffer, argv[1]);` copies the first argument of the program into the variable `buffer[100]` without specifying the maximum number of bytes to be copied (in this case 100) ==> the buffer can be overflowed
* we observe that the variable `command[10]` which contains the actual command that is run by the program is declared before the variable `buffer[100]`. This means that most likely the content of `command` will follow the content of the `buffer` in the stack.

Therefore, the stack would look like this:
```plaintext
+---------------------------+ higher addresses
| ...                       |
+---------------------------+
| return address            |        |
+---------------------------+        |
| base pointer              |        | stack growth
+---------------------------+        |
| command[10]               |        |
+---------------------------+        V
| alignment padding (maybe) |
+---------------------------+
|buffer[100]                |
+---------------------------+  lower addresses
```

It is now clear that we need to write at least 100 characters to overwrite the buffer and we need to check if there is any padding between the the buffer location and the command location. We do this by providing input longer than 100 and observe how the output is affected. 

Turns out the padding is 2 bytes and an input that spawns a shell is:
```sh
 ./buffer $(perl -e 'print "a"x102 . "/bin/sh"')
 ```


## Exercise 2: normal version
In this exercise we need to figure out what a program does without having the source code. We will use gdb for this, and the fist step will be to mark the downloaded file as executable to be able to run it inside gdb: `chmod +x pwd-normal` 

a) We start gdb, then load our program and start it in debugging mode using the following commands:
```sh
$gdb
...
(gdb) file pwd-normal 
Reading symbols from pwd-normal...
(gdb) start
Temporary breakpoint 1 at 0x401c4e: file main.c, line 20.
```
Note that after the `start` command a temporary break point is set automatically at the beginning of the function `main`.

### Information gathering
* we can run the program (by writing `continue` inside gdb) and get a high level intuition about what it is doing. We are then required a password and by introducing a random one, the program terminates with the message: Wrong password. (to run it again, write `start`) 
* by restarting the program and running the command `(gdb) info variables` we find out that the main function contains 3 variables:
    ```C
    buf = "`f@\000\000\000\000\000\000g@\000\000\000\000\000\000\000\000"
    ok = 0
    i = 4890648
    ```
    We observe that `buf` is an array of 19 bytes. (\000 is 1 byte).
* we can now take a look inside the main function by typing `(gdb) disassemble main`. Depending on the preference, before running this command we could set the assembly style from att to intel: `(gdb) set disassembly-flavor intel`. Here we can search for the `call` instructions to get information over the functions called from within `main`: printf, gets, sha256, hash_equals, puts.

### Disassemble main
 
 To be continued ...
 ....


b) An input that bypasses the password is `aaaabbbbccccddddeeeeffffggggh` aka 29 characters which overrites the variable OK with a non-zero number, therefore the verification becomes true and the message "You're root!" is obtained. 

