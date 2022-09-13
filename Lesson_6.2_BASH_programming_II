UNIX Lesson 6.2: BASH Programming II
===================



## Arrays

Arrays in Bash are ordered lists of values. You can create a list from scratch
by assigning it to a variable name. Lists are created with parentheses (`( )`)
with a space separating each element in the list. Let's make a list of the
plagues of Egypt:


```bash
colors=(red blue green yellow pink brown black white cyan)
```

To retrieve the array you need to use **parameter expansion**, which involves
the dollar sign and curly brackets (`${ }`). The positions of the elements in
the array are numbered starting from zero. To get the first element of this
array use `${plagues[0]}` like so:


```bash
echo ${colors[0]}
```

```
## red
```

Notice that the first element has an **index** of 0. You can get any of the
elements this way, for example the fourth element:


```bash
echo ${colors[3]}
```

```
## yellow
```

To get all of the elements of `colors` use a star (`*`) between the square
brackets:


```bash
echo ${colors[*]}
```

```
## red blue green yellow pink brown black white cyan
```

You can also change an individual elements in the array by specifying their
index with square brackets:


```bash
echo ${colors[*]}
plagues[4]=magenta
echo ${colors[*]}
```

```
## red blue green yellow pink brown black white cyan
## red blue green yellow magenta brown black white cyan
```

To get only part of an array you have to specify the index you would like to
start at, followed by the number of elements you would like to retrieve from the
array, separated by colons:


```bash
echo ${colors[*]:5:7}
```

```
## brown black white
```

The above query essentially says: get 3 array elements starting from the sixth
element of the array (remember, the sixth element has an index of 5).

You can find the length of an array using the pound sign (`#`):


```bash
echo ${#colors[*]}
```

```
## 10
```

You can use the plus-equals operator (`+=`) to add an array onto the end of
an array array:


```bash
numbers=(1 2 3 4)
echo ${numbers[*]}
numbers +=(5 6 7)
echo ${numbers[*]}
```

```
## 1 2 3 4
## 1 2 3 4 5 6 7
```

### Summary

- Arrays are a linear data structure with ordered elements which can be stored
in variables.
- The each element of an array has an index and the first index is 0.
- Individual elements of an array can be accessed using their index.

### Exercises

1. Write a bash script where you define an array inside of the script, and the
first argument for the script indicates the index of the array element that is
printed to the console when the script is run.
2. Write a bash script where you define two arrays inside of the script, and the
sum of the lengths of the arrays are printed to the console when the script is
run.

<br />

## Braces

Bash has a very handy tool for creating strings out of sequences called
**brace expansion**. Brace expansion uses the curly brackets and two periods
(`{ .. }`) to create a sequence of letters or numbers. For example to create a
string with all of the numbers between zero and nine you could do the following:


```bash
echo {0..9}
```

```
## 0 1 2 3 4 5 6 7 8 9
```

In addition to numbers you can also create sequences of letters:


```bash
echo {a..e}
echo {W..Z}
```

```
## a b c d e
## W X Y Z
```

You can put strings on either side of the curly brackets and they'll be "pasted"
onto the corresponding end of the sequence:


```bash
echo a{0..4}
echo b{0..4}c
```

```
## a0 a1 a2 a3 a4
## b0c b1c b2c b3c b4c
```

You can also combine sequences so that two or more sequences are pasted
together:


```bash
echo {1..3}{A..C}
```

```
## 1A 1B 1C 2A 2B 2C 3A 3B 3C
```

If you want to use variables in order to define a sequence you need to use the
`eval` command in order to create the sequence:


```bash
start=4
end=9
echo {$start..$end}
eval echo {$start..$end}
```

```
## {4..9}
## 4 5 6 7 8 9
```

You can combine sequences with a comma between brackets (`{,}`):


```bash
echo {{1..3},{a..c}}
```

```
## 1 2 3 a b c
```

In fact you can do this with any number of strings:


```bash
echo {Who,What,Why,When,How}?
```

```
## Who? What? Why? When? How?
```

### Summary

- Braces allow you create string sequences and expansions.
- To use variables with braces you need to use the `eval` command.

### Exercises

1. Create 100 text files using brace expansion.

<br />

## Loops

### `for`

Loops are one of the most important programming structures in the Bash language.
All of the programs we've written so far are executed from the first line of the
script until the last line, but loops allow you to repeat lines of code based on
logical conditions or by following a sequence. The first kind of loop that we'll
discuss is a FOR loop. **FOR loops** iterate through every element of a sequence
that you specify. Let's take a look at a small example FOR loop:

```
#!/usr/bin/env bash
# File: forloop.sh

echo "Before Loop"

for i in {1..3}
do
	echo "i is equal to $i"
done

echo "After Loop"
```

Now let's execute this script:


```bash
bash forloop.sh
```

```
## Before Loop
## i is equal to 1
## i is equal to 2
## i is equal to 3
## After Loop
```

Once you've experimented a little take a look at this example with several
other kinds of sequence generating strategies:

```
#!/usr/bin/env bash
# File: manyloops.sh

echo "Explicit list:"

for picture in img001.jpg img002.jpg img451.jpg
do
	echo "picture is equal to $picture"
done

echo ""
echo "Array:"

stooges=(curly larry moe)

for stooge in ${stooges[*]}
do
	echo "Current stooge: $stooge"
done

echo ""
echo "Command substitution:"

for code in $(ls)
do
	echo "$code is a bash script"
done
```


```bash
bash manyloops.sh
```

```
## Explicit list:
## picture is equal to img001.jpg
## picture is equal to img002.jpg
## picture is equal to img451.jpg
##
## Array:
## Current stooge: curly
## Current stooge: larry
## Current stooge: moe
##
## Command substitution:
## bigmath.sh is a bash script
## condexif.sh is a bash script
## forloop.sh is a bash script
## letsread.sh is a bash script
## manyloops.sh is a bash script
## math.sh is a bash script
## nested.sh is a bash script
## simpleelif.sh is a bash script
## simpleif.sh is a bash script
## simpleifelse.sh is a bash script
## vars.sh is a bash script
```

The example above illustrates three other methods of creating sequences for FOR
loops: typing out an explicit list, using an array, and getting the result of a
command substitution. In each case a variable name is declared after the `for`,
and the value of tha variable changes through each iteration of the loop until
the corresponding sequence has been exhausted. 

Right now you should take a moment to write a few FOR loops yourself, generating sequences in all of the ways that we've gone over, just to reinforce your understanding of how a FOR loop works. 


**excercise**: In bioinformatics, k-mers are substrings of length *k* contained within a biological sequence. Usually, the term *k-mer* refers to all of a sequence's subsequences of length *k*, such that the sequence AGAT would have four monomers (A, G, A, and T), three 2-mers (AG, GA, AT), two 3-mers (AGA and GAT) and one 4-mer (AGAT)


Try to make a script in bash that generate all possible 3-kmers with (A G T C) bases.


<br />

### `while`

Now that we've gotten a few FOR loops working let's move on to WHILE loops. The
**WHILE loop** combine parts of the FOR loop and the IF statement.
Let's take a look at an example WHILE loop so you can see what I mean:

```
#!/usr/bin/env bash
# File: whileloop.sh

count=3

while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count-1
done
```

The WHILE loop begins first with the `while` keyword followed by a conditional
expression. As long as the conditional expression is equivalent to `true` when
an iteration of the loop begins, then
the code within the WHILE loop will continue to be executed. Based on the code
for `whileloop.sh` what do you think will be printed to the console when we run
this script? Let's find out:


```bash
bash whileloop.sh
```

```
## count is equal to 3
## count is equal to 2
## count is equal to 1
```

Before the WHILE the `count` variable is set to be 3, but then each
time the WHILE loop is executed 1 is subtracted from the value of `count`. The
loop then starts from the top again and the conditional expression is
re-checked to see if it's still equivalent to `true`. After three iterations
through the loop `count` is equal to 0 since 1 is subtracted from `count` in
every iteration. Therefore
the logical expression `[[ $count -gt 0 ]]` is no longer equal to `true` and
the loop ends. By changing the value of the variable in the logical expression
inside of the loop we're able to ensure that the logical expression will
eventually be equivalent to `false`, and therefore the loop will eventually end.

If the logical expression is never equivalent to `false` then we've created an
*infinite loop*, so the loop never ends and the program runs forever. Obviously we
would like for our programs to end eventually, and therefore creating infinite
loops is undesirable. However let's create an infinite loop so we know what to
do if we get into a situation where our program won't terminate. With a simple
"typo" we can change the program above so that it runs forever but substituting
the minus sign `-` with a plus sign `+` so that `count` is always greater than
zero (and growing) after every iteration.

```
#!/usr/bin/env bash
# File: foreverloop.sh

count=3

while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count+1              # We only changed this line!
done
```

```
## ...
## count is equal to 29026
## count is equal to 29027
## count is equal to 29028
## count is equal to 29029
## count is equal to 29030
## ...
```

If the program is working, then `count` is being incremented very rapidly and
you're watching numbers piling up in your terminal! Don't fret, you can terminate
any program that's stuck in an infinite loop using `Control` + `C`. Use
`Control` + `C` to get the prompt back so that we can continue.

When constructing WHILE loops, make absolutely sure that you've structured the
program so that the loop will terminate! If the logical expression after `while`
never becomes `false` then the program will run forever, which is probably not
the kind of behavior you were planning for your program.

### Nesting

Just like IF statements `for` and `while` loops can be nested within each other.
In the example below an IF loop nested inside of another FOR loop:


```
#!/usr/bin/env bash
# File: ifloop.sh

for number in {1..10}
do
  if [[ $number -lt 3 ]] || [[ $number -gt 8 ]]
  then
    echo $number
  fi
done
```

Before we run this example try once more to guess what the output will be.


```bash
bash ifloop.sh
```

```
## 1
## 2
## 9
## 10
```

For each iteration of the loop above, the value of `number` was checked in the
IF statement, and the `echo` command was only run if `number` was outside the
range from 3 to 8.



### Summary

- Loops allows you repeat sections of your program.
- FOR loops iterate through a sequence so that a variable that you assign
takes on the value of every element of the sequence in every iteration of the
loop.
- WHILE loops check a conditional statement at the beginning of every iteration.
If the condition is equivalent to `true` then one iteration of the loop is
executed and then the conditional statement is checked again. Otherwise the
loop ends.
- IF statements and loops can be nested in order to make more powerful
programming structures.

### Exercises

- Write several programs with three levels of nesting and include FOR loops,
WHILE loops, and IF statements. Before you run your program try to predict what
your program is going to print. If the result is different from your prediction
try to figure out why.
- Enter the `yes` command into the console, then stop the program from running.
Take a look at the `man` page for `yes` to learn more about the program.



## Reading files

Although the for loop is very useful for iterating over files in directories or keeping track of numbers, it does not allow us to iterate in a classic way over the lines of a text file. If we try to read a file line by line and use a “for” loop, (for line in $(cat file.txt); do...) what we do is an evaluation of each word and not each line:

```
$ cat file.txt
This is the line 1
This is the line 2
```

```
for line in $(cat file.txt);do
  echo ${line}
done
```

```
 
$ bash script.sh
This
is
the
line
1
This
is
the
line
2 
```

To read line by line a file we can use the `read` command in a while loop as you can see below:

```bash
#!/usr/bin/env bash
# File: read_loop.sh

cat file.txt | while read line
do
  echo  "$line"
done

// this other way also work //
#!/usr/bin/env bash
# File: read_loop.sh

while read line; do
  echo "$line"
done < file.txt
``` 

``` bash 
> read_loop.sh
This
is
the
line
1
This
is
the
line
2
```



## Functions

### Writing Functions

A function is a small piece of code that has a name. Writing functions allows
us to re-use the same code multiple times across programs. Functions have the
the following syntax:

```
function [name of function] {
  # code here
}
```

Pretty simple, right? Let's open up a new file called `hello.sh` so we can write
our first simple function.

```
#!/usr/bin/env bash
# File: hello.sh

function hello {
  echo "Hello"
}

hello
hello
hello
```

The entire structure of the function including the `function` keyword, the name
of the function, and the code for the function written inside of the brackets
serves as the **function definition**. The function definition assigns the code
within the function to the name of the function (`hello` in this case). After a
function is defined it can be used like any other command. Using our `hello`
command three times should be the equivalent of using `echo "Hello"` three
times. Let's run this script to find out:


```bash
bash hello.sh
```

```
## Hello
## Hello
## Hello
```

It looks like this function works exactly like we expected.

Functions share lots of their behavior with individual bash scripts including
how they handle arguments. The usual bash script arguments like `$1`, `$2`, and
`$@` all work within a function, which allows you to specify function arguments.
Let's create a slightly modified version of `hello.sh` which we'll call
`hello2.sh`:

```
#!/usr/bin/env bash
# File: hello2.sh

function hello {
  echo "Nice to meet you $1"
}
hello mark
hello juan
```

```bash
bash hello2.sh
"Nice to meet you mark"
"Nice to meet you juan"
```


Let's write a more complicated function. Imagine that we wanted to add up
a sequence of numbers from the command line, but we had no way of knowing how
many numbers would be in the sequence. What components would we need to write
this function? First we would need a way to capture a list of arguments which
can have variable length, second we would need a way to iterate through that
list so we could add up each element, and we would need a way to store the
acumulative sum of the sequence. These three requirements can be satisfied by
using the `$@` variable, a FOR loop, and variable where we can store the sum.
It's important to break down a larger goal into a series of individual
components before writing a program, that way we more easily can identify which
features and tools will be required. Let's write this program in a file called
`addseq.sh`.

```
#!/usr/bin/env bash
# File: addseq.sh

function addseq {
  sum=0

  for element in $@
  do
    let sum=sum+$element
  done

  echo $sum
}
```

In the program above we initialize the `sum` variable to be 0 so that we can
add other values in the sequence to `sum`. We then use a FOR loop to iterate
through every element of `$@`, which is an array of all the arguments we provide
to `addseq`. Finally we `echo` the value of `sum`. Let's `source` this program
and test it out:


```bash
source addseq.sh
addseq 12 90 3
addseq 0 1 1 2 3 5 8 13
addseq
addseq 4 6 6 6 4
```

```
## 105
## 33
## 0
## 26
```

### Summary

- Functions start with the `function` keyword followed by the name of the
function and curly brackets (`{}`).
- Functions are small, reusable pieces of code that behave just like commands.
- You can use variables like `$1`, `$2`, and `$@` in order to provide arguments
to functions, just like a Bash script.
- Be sure to `echo` the results of your function (if there are any) so that
they can be captured with command substitution.

### Exercises

Below this list of exercises you can find examples of how these programs should
work when used on the command line.

1. Write a function called `plier` which multiplies together a sequence of
numbers.
2. Write a function called `isiteven` that prints `1` if a number is even or
`0` a number is not even.



