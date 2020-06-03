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
| return address            |
+---------------------------+ |
| base pointer              | | stack growth
+---------------------------+ |
| command[10]               | |
+---------------------------+ V
| alignment padding (maybe) |
+---------------------------+
|buffer[100]                |
+---------------------------+ lower addresses
```

It is now clear that we need to write at least 100 characters to overwrite the buffer and we need to check if there is any padding between the the buffer location and the command location. We do this by providing input longer than 100 and observe how the output is affected. 

Turns out the padding is 2 bytes and an input that spawns a shell is:
```sh
./buffer $(perl -e 'print "a"x102 . "/bin/sh"')
```

## Exercise 2: bypass password verification with gdb 

## I. The normal version
In this exercise we need to figure out what a program does without having the source code. We will use gdb for this, and the first step will be to mark the downloaded file as executable to be able to run it inside gdb: `chmod +x pwd-normal` 

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
* we can run the program (by writing `continue` inside gdb) and get a high level intuition about what it is doing. We are required a password and by introducing a random one, the program terminates with the message: Wrong password. (to run it again, write `start`) 
* by restarting the program and running the command `(gdb) info variables` we find out that the main function contains 3 variables:
```C
buf = "`f@\000\000\000\000\000\000g@\000\000\000\000\000\000\000\000"
ok = 0
i = 4890648
```
We observe that `buf` is an array of 19 bytes. (\000 is 1 byte).
* we can now take a look inside the "main" function by typing `(gdb) disassemble main`. Depending on the preference, before running this command we could set the assembly style from att (default) to intel: `(gdb) set disassembly-flavor intel`. Here we can search for the `call` instructions to get information over the functions called from within `main`: printf, gets, sha256, hash_equals, puts.

### Disassemble main
Below we can see the disassembled code for the `main` function. The comments on the right side describe what the instructions accomplish. If you are not so familiar with assembly, you could use the `step` and `ni` command (see gdb documentation) to take one step at a time. Then you could immediately check the values of the local variables (`info locals`) and observe if any of them changed and try to see why. You could also set breakpoints in the code, then by pressing `continue` the execution will stop at that particular point. In order to set breakpoints we use the command `b *address`, where for this particular example the address is the long number that begins with 0x in front of an instruction (below it is omitted).
Another useful gdb command is `x/s address` which help us read strings from a specific memory location. For example, here we can see the location of the string "You're root!"


```assembly
Dump of assembler code for function main:
...46 <+0>: push rbp
...47 <+1>: mov rbp,rsp
...4a <+4>: sub rsp,0x20                                    |->allocate 32 bytes on the stack
...4e <+8>: mov DWORD PTR [rbp-0x4],0x0                     |-> set ok and i to 0 
...55 <+15>: mov DWORD PTR [rbp-0x8],0x0                   _|_
...5c <+22>: jmp 0x401c6c <main+38>                         |
...5e <+24>: mov eax,DWORD PTR [rbp-0x8]                    |
...61 <+27>: cdqe                                           |
=> ...63 <+29>: mov BYTE PTR [rbp+rax*1-0x20],0x0           |-> for i=0 to 19 
...68 <+34>: add DWORD PTR [rbp-0x8],0x1                    | buf[i] = 0
...6c <+38>: cmp DWORD PTR [rbp-0x8],0x13                   |
...70 <+42>: jle 0x401c5e <main+24>                        _|_
...72 <+44>: lea rdi,[rip+0x803c7] # 0x482040               |->printf("Please enter your password")
...79 <+51>: mov eax,0x0                                    |
...7e <+56>: call 0x40c880 <printf>                        _|_ 
...83 <+61>: lea rax,[rbp-0x20]                             |-> load in rax the address of buffer
...87 <+65>: mov rdi,rax                                    |
...8a <+68>: mov eax,0x0                                    |
...8f <+73>: call 0x40d380 <gets>                          _|_-> read password into buffer
...94 <+78>: lea rax,[rbp-0x20] |-> rax = buffer address
...98 <+82>: mov edx,0x14 |-> edx = 20 (size of buffer +1)
...9d <+87>: mov rsi,rax |-> rsi = buffer address 
...a0 <+90>: lea rdi,[rip+0xaa659] # 0x4ac300 <hash>
...a7 <+97>: call 0x40573a <sha256> _|_->compute hash of password and put it into address 0x4ac300 <hash>
...ac <+102>: lea rsi,[rip+0x8036d] # 0x482020 <okhash> | 
...b3 <+109>: lea rdi,[rip+0xaa646] # 0x4ac300 <hash> |-> compare computed hash with correct hash
...ba <+116>: call 0x401bf5 <hash_equals> _|_ and return result
...bf <+121>: test eax,eax |-> if result of hash_equals is not 0 
...c1 <+123>: je 0x401cca <main+132> | ok == 1 
...c3 <+125>: mov DWORD PTR [rbp-0x4],0x1 | if ok ==0 
...ca <+132>: cmp DWORD PTR [rbp-0x4],0x0 | then print wrong pass and exit # 0x48206a
...ce <+136>: je 0x401cde <main+152> | else 
...d0 <+138>: lea rdi,[rip+0x80386] # 0x48205d | print You're root! # 0x48205d
...d7 <+145>: call 0x40d4f0 <puts> |
...dc <+150>: jmp 0x401cea <main+164> |
...de <+152>: lea rdi,[rip+0x80385] # 0x48206a | 
...e5 <+159>: call 0x40d4f0 <puts> _|_
...ea <+164>: mov eax,0x0
...ef <+169>: leave 
...f0 <+170>: ret 
```

b) From line <+4>: in the disassembled main, we know that there were allocated 32 bytes for the stack. We also know that the buffer address is the same as the the stack pointer. What we also see is that the `ok` variable is situated next to the base pointer and it has 4 bytes (see line <+8> and <+132> ). Therefore we need 32-4+1=29 characters to overwrite the variable `ok` with a non-zero value, such that the verification from line <+132> becomes true and the message "You're root!" is obtained. An input that bypasses the password is `aaaabbbbccccddddeeeeffffggggh`. 

## II. The hard version
In the hard version of the exercise there is no information about the program variables. Therefore the command `info variables` does not offer anything. The approach for this version is to disassemble the `main` function just like before and analyze the assembly line by line. We can still see the function names and look into the memory for strings (with `x/s address`) which gives us an intuition of the program flow. Here, even if we do not have the variable names we can see that at the top of the stack (position `rbp-0x20`)there is a buffer of size 19 (see lines <+22>: to <+42>:) that is updated byte by byte. We can also see that depending on the value of the variable situated at the position `rbp-0x4` we become root or not (if the value is non zero). Following the same logic as before, we can deduce that a 29-byte input will get us to root. 


