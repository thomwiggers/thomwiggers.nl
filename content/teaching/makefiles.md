+++
title = "Makefiles: recipes for binaries"
date = 2018-12-21
summary = "Some notes on writing Makefiles"

draft = false
toc = true
type = "docs"

highlight = true
highlight_languages = ["c", "makefile", "shell", "plaintext"]

[menu.teaching]
  name = "Makefile"
  weight = 2
  parent = "Hacking in C"
+++


Writing `Makefile`s is like writing a recipe.
It consists of ingredients and a list of procedures to turn those ingredients into a product.
In this tutorial, I will briefly cover how this works.
We'll first look at how we might turn a recipe for an apple pie from a cookbook into a `Makefile`.

## Making an apple pie

A recipe to cook an apple pie[^pie] might look as follows:

[^pie]: I mostly made up the ingredients, so it may not be a good idea to serve a pie you made using this recipe to your grandmother or lecturer.

> ### Ingredients
> 
> * 200 grams of butter
> * 20 grams of sugar
> * 400 grams of self-raising flower
> * egg
> * 8 grams of vanilla sugar
> * salt
> * 1 Kg apples
> * 75 grams of raisins
> * cinnamon
> 
> ### Making the pie
> 
> #### Melting the butter
> 1. Put the butter in a microwave and slowly melt it, stir it once in a while
> 
> #### Making the dough 
> _Prequisites: melting the butter_
> 
> 1. Mix the molten butter, the flower and 2/3s of the egg
> 2. Knead the dough until it's consistent
> 
> #### Preparing the raisins
> 1. Put the raisins in lukewarm water
> 2. Wait 15 minutes
> 3. Dry them off
> 
> #### Preparing the apples
> 1. Skin the apples 
> 2. dice them
> 
> #### Making the filling
> _Prequisites: preparing the raisins, preparing the apples_
> 
> 1. Mix the diced apples with the sugar and the prepared raisins
> 
> 
> #### Making the pie
> _Prequisites: Making the dough, making the filling_
> 
> 1. Cover the springform using 2/3s of the dough
> 2. Put the filling in the pie
> 3. Cover the pie with the remainder of the dough
> 
> #### Baking the pie
> _Prequisites: Making the pie_
> 
> 1. Put the pie in the oven that's been pre-heated to 200 degrees Celcius
> 2. Take it out after 60 minutes

I've split this recipe up into more steps than you may be used to.
I did this to illustrate that you have certain parts of the process of _building_ an apple pie product that you can separate.
These parts may have dependencies on prior parts of the process, though.
For example, you can not make the filling before you prepared the apples and the raisins.

## Turning the recipe into a Makefile

A `Makefile` also consists of (intermediate) _products_, _recipes_ and _prequisites_.
It has the following structure:

```Makefile
product: ingredient1 ingredient2 prequisite1
	recipe that combines prequisite1 with ingredient1 and ingredient2

prequisite1: ingredient3 ingredient1
	recipe for prequisite1
```

`make` can use these rules to create `product` for you.
It will also figure out whenever it needs to do something again, mainly if an ingredient or a prequisite changed.

So now let us change our apple pie recipe into something `make` would be able to understand:

```Makefile
pie: prepared_pie
	put prepared_pie into oven
	wait 60 minutes
	take it out

prepared_pie: dough filling
	cover springform with 2/3s of dough
	put filling in
	close off pie with the remainder of the dough

filling: sugar prepared_raisins prepared_apples
	Mix the apple with the sugar and the prepared raisins

prepared_raisins: raisins
	Put the raisins in lukewarm water
	Wait 15 minutes
	Dry them off

prepared_apples:
	Skin the apples
	Dice the apples

dough: molten_butter flower egg
	Mix the molten butter, the flower and the egg
	Knead until consistent

molten_butter: butter
	Put the butter in the microwave on low until it's molten
```

* **Note**: I put `pie:` at the top, because `Make` will try to build the top-most _target_ (_product_).
Otherwise the order is not important.

## Moving to code
In our apple pie `Makefile` we can identify that we have different (intermediate) products or _targets_ that have some steps associated to prepare them,
and some of these depend on others or on ingredients.
We specify this so that Make can figure out when it needs to update something.
Of course, "updating sugar" makes no sense, so lets look at an example where we have a source file.

### A simple example

```shell
/tmp/src $ ls
hello.c
```

```c
#include<stdio.h>

void say_hello() {
    puts("Hello, world!");
}

int main(int argc, char** argv) {
    say_hello();
}
```

We could build this using the following `gcc` shell command:

```
/tmp/src $ gcc -o hello hello.c
/tmp/src $ ./hello
Hello, world!
```

But lets write a simple `Makefile`.
We are lazy and want to be able to just type `make`.

```
/tmp/src $ touch Makefile  # Should have a capital M!
/tmp/src $ edit Makefile
```

Then we enter the following as our build recipe:

```Makefile
hello: hello.c
	gcc -o hello hello.c
```

**Important**: `Makefile` rules **must** be indented with **tabs**, not spaces. Make sure you configure your editor correctly!

Lets see if this works:

```shell
/tmp/src $ make
make: 'hello' is up to date.
```

Huh? `make` didn't do anything!
It turns out that `make` is quite smart, and it realised that `hello` has a more recent modification date than `hello.c`.
That usually means that there's no good reason to do all that work of compiling `hello.c` again, so `make` just doesn't do it.
We can force it to build things using `make -B`, or we can remove `hello`. Let us do that:

```shell
/tmp/src $ rm hello
/tmp/src $ make
gcc -o hello hello.c
/tmp/src $ ./hello
Hello, world!
```

Neat!

### A more complicated example

So far, our example was very basic. `make` shines when you have a more complicate build process.
Lets extend our example to have more than one source file, which we want to build and link separately.
This allows us to only recompile what has been changed, while we are developing the project.

Let us set up two source files in our `/tmp/src` folder:

```c
// hello.c
// we use extern to indicate that we will specify say_hello() elsewhere.
extern void say_hello();

int main(int argc, char** argv) {
    say_hello();
}
```

```c
// say_hello.c
#include <stdio.h>

void say_hello() {
    puts("Hello, world! from say_hello.c");
}
```

We can build and link these files as follows

```shell
/tmp/src $ gcc -c -o hello.o hello.c
/tmp/src $ gcc -c -o say_hello.o say_hello.c
# Note that in the next line we use the compiled `.o` files!
/tmp/src $ gcc -o hello hello.o say_hello.o
/tmp/src $ ./hello
Hello, world! from say_hello.c
```

Clearly, this is way too much work to type.
We can write a `Makefile` to save us all this work.

```Makefile
hello: hello.o say_hello.o
	gcc -o hello hello.o say_hello.o

hello.o: hello.c
	gcc -c -o hello.o hello.c

say_hello.o: say_hello.c
	gcc -c -o say_hello.o say_hello.c
```

We made three rules: one to build the final target `hello`, and two to build its prequisites `hello.o` and `say_hello.o`.
Lets test our `Makefile`:

```shell
/tmp/src $ make
make: target 'hello' is up to date.
```

Oh, right… We got outsmarted by `make`s lazyness again. Lets force `make` to rebuild everything.

```shell
/tmp/src $ make -B
gcc -c hello.c -o hello.o
gcc -c say_hello.c -o say_hello.o
gcc -o hello hello.o say_hello.o
/tmp/src $ ./hello
Hello, world! from say_hello.c
```

That worked great!
We can now also see that `make` is smart, if we change for example `say_hello.c`.
Lets change `say_hello()`:

```c
void say_hello() {
    puts("Hello, world! from say_hello.c");
    puts("And goodbye again");
}
```

Now we can run `make` again:

```shell
/tmp/src $ make
gcc -c say_hello.c -o say_hello.o
gcc -o hello hello.o say_hello.o
```

`make` realised that only `say_hello.c` changed and only rebuild `say_hello.o`.
As a result of that, it also needed to link `hello` again, but it **skipped** building `hello.o`!
It's easy to see that as your program grows, this can be very helpful.[^parallel]

[^parallel]: Splitting up build steps also allows `Make` to do things in parallel. See `man make` for more information.

## Common problems and caveats

Finally, lets discuss some of the problems you may run into.

### Makefile template
As a reminder, your `Makefile` should look as follows:

```Makefile
target: ingredients
	build rules indented with **TAB**
```

`target` should normally be something on the filesystem, unless you want to always have it execute when you try to build it.
`ingredients` should be other `target`s or files on the filesystem.

### Indentation
`Makefile`s **must** be indented with **tabs**. If you indent them with spaces you may get errors

```shell
Makefile: 2: *** missing separator.  Stop.
```

### Already up to date

`make` is lazy and sees that your binaries are more recent than your source files.
If you want to force a rebuild, use `make -B`, change the source files, or remove the targets.

### No rule to make target

If you specify something that `make` can not find on the filesystem or does not know how to build from other things, it will complain.
For example:

```Makefile
say_hello.o: zay_hello.c
	gcc -c say_hello.c -o say_hello.o
```

We made a typo in `say_hello.c` when we specified the ingredients for `say_hello.o`.
This results in the error:

```shell
make: *** No rule to make target 'zay_hello.c', needed by 'say_hello.o'.  Stop.
```

We can fix this by repairing the typo.

This can also apply to targets that depend on _other_ targets:

```Makefile
hello: hello.o zay_hello.o
	gcc -o hello hello.o say_hello.o
```

Then `make` will also complain:
```
make: *** No rule to make target 'zay_hello.o', needed by 'hello'.  Stop.
```

We can solve this by writing a rule for `zay_hello.o`, that renames `say_hello.o` to `zay_hello.o`:

```Makefile
zay_hello.o: say_hello.o
	mv say_hello.o zay_hello.o
```

But that is a bit silly. 
Better fix the typo, in this case.

### No targets specified and no makefile found.

This error occurs if you don't have a `Makefile` in your current folder.
Check if a `Makefile` exists, the name is spelled correctly (exactly `Makefile`) and make sure it has a capital `M`!
