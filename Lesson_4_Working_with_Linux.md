UNIX 4: Working with UNIX
===================


## 5.1 Get Wild

`Wildcards` are useful in many ways for a GNU/Linux system and for various other uses. Commands can use wildcards to **perform actions on more than one file at a time**, or **to find part of a phrase in a text file**.

<br />

First of all we have to download the script `generate_sequences.sh` stored in **resources/** folder in this repository. Save the script in the bioinformatic_course folder. To run the script type:

```BASH
bash generate_sequences.sh
```

This script will generate some genes files in a new directory named **sequences**

<br />

Let's go into my `sequences` folder in my home directory and take a look around:


```bash
pwd
```

```
## /Users/jgl
```


```bash
ls
```

```
## Code
## Documents
## Desktop
## bioinformatic_course
## Projects
```


```bash
cd bioinformatic_course
cd sequences
ls
```

```
## geneA_01.fn
## geneA_02.fn
## geneA_03.fasta
## geneA_04.fn
## geneB_01.fn
## geneB_02.fn
## geneC_01.fn
## geneC_02.fasta
## geneC_03.fn
## geneC_04.fn
## geneD_01.fn
## geneD_02.fasta
## geneE_01.fn
## geneF_01.fn
```

In sequences folder Im currently save last genes I have sequenced without any organization.
Instead of using `mv` to move around each
individual sequence I can select groups of genes using the `*` wildcard. A 
**wildcard is a character that represents other characters**, much like how
joker in a deck of cards can represent other cards in the deck. Wildcards are
a subset of **metacharacters**, a topic which we will discuss in detail later on in
this Lesson. 

### The ```*```

The `*` ("star") **wildcard** represents ***zero or more of any
character***, and it can be used to match names of files and folders in the 
command line. For example if I wanted to list all of the files in my sequences 
directory which have a name that starts with "geneA" I could do the following:


```bash
ls geneA*
```

```
## geneA_01.fn
## geneA_02.fn
## geneA_03.fasta
## geneA_04.fn
```

Only the files starting with "geneA" are listed! The command `ls geneA*` literally
means: ***list the files that start with "geneA" followed by zero or more of any
character***. As you can imagine using wildcards is a powerful tool for working 
with groups of files that are similarly named.

We could only list the sequences files starting with "geneB":


```bash
ls geneB*
```

```
## geneB_01.fn
## geneB_02.n
```

We could list only the files with names ending in `.fasta`:


```bash
ls *.fasta
```

```
## geneA_03.fasta
## geneC_02.fasta
## geneD_02.fasta
```

In the case above the file name can belong to diferent version of the sequence (01, 02, 03, ..), but the file name must end in `.fasta`.
So we could also list only the first version of each set of genes:


```bash
ls *_01.*
```

```
## geneA_01.fn
## geneB_01.fn
## geneC_01.fn
## geneD_01.fn
## geneE_01.fn
## geneF_01.fn
```

All of the files above have names that are composed of a sequence of characters,
followed by the adjacent characters `_01.`, followed by another sequence of
characters.
Notice that if I had entered `ls *_0*` into the console every file would have
been listed since `_0` is a part of all of the file names in my sequences
directory.


Let's organize these sequence by gene. First let's create one directory for each gene:


```bash
mkdir geneA
mkdir geneB
mkdir geneC
mkdir geneD
mkdir geneE
mkdir geneF
```

Now we can move the photos using wildcards:


```bash
mv geneA_* geneA/
ls
```

```
## geneA/
## geneB/
## geneB_01.fn
## geneB_02.fn
## geneC/
## geneC_01.fn
## geneC_02.fasta
## geneC_03.fn
## geneC_04.fn
## geneD/
## geneD_01.fn
## geneD_02.fasta
## geneE/
## geneE_01.fn
## geneF/
## geneF_01.fn

```

Notice that I've moved all files that start with "geneA_" into the geneA/ folder!
Now let's do the same thing for files with names starting with "geneB":


```bash
mv geneB_* geneB/
ls
```

```
## geneA/
## geneB/
## geneC/
## geneC_01.fn
## geneC_02.fasta
## geneC_03.fn
## geneC_04.fn
## geneD/
## geneD_01.fn
## geneD_02.fasta
## geneE/
## geneE_01.fn
## geneF/
## geneF_01.fn
```

Finally my sequences have started to be somewhat organized! Let's list the files in one of these directories
just to make sure all was moved as planned:


```bash
ls geneA/
```

```
## geneA_01.fn
## geneA_02.fn
## geneA_03.fasta
## geneA_04.fn
```


```bash
ls geneB/
```

```
## geneB_01.fn
## geneB_02.fn
```

Looks good! There are a few more wildcard, let's see

### The ```?```


```?```(question mark) wildcard represent ***any single character***. If you specified something like ```geneA_0?.fa``` you will return all the geneA files with .fa extension:

```
ls geneA_0?.fa
```

```
## geneA_01.fn
## geneA_02.fn
## geneA_04.fn

```

### The ```[ ]```

```[]``` **Specifies a range**. If you did geneA_intron_[1,2,3].fasta it can become: geneA_intron_1.fasta, geneA_intron_2.fasta and  geneA_intron_3.fasta ,  it can become anything that starts with 'geneA_intron_' and ends with '_.fasta_'. This kind of wildcard specifies an “or” relationship (you only need one to match) For example, these would work:


```
ls geneE_0[1,2,3,4].fa
geneE_01.fa
```




### The```{ }```

Another important wildcard is ```{ }``` (curly brackets). In this case you can specifies a list of terms separated by commas and each term must be a name of something or a wildcard. For example, imagine you want to print a set of serially numbered files for 5 imaginary genes:


```
echo gene_{A1,A2,A3,A4,A5}
gene_A1 gene_A2 gene_A3 gene_A4 gene_A5
```
You can combine the list emcapsuled in ```{}``` wildcard adding characters at both the bigining and the end of the ```{}```, let's see:  

```
echo gene_{1,2,3,4,5}.fa
gene_1.fa gene_2.fa gene_3.fa gene_4.fa gene_5.fa
```




### Summary

- Wildcards can represent many kinds and numbers of characters.
- You can use wildcards on the command line in order to work with multiple files and folders.

| Wildcard	   |               Meaning                |
|--------------:|:-------------------------------------|
|  ```*```      |      zero or more of any character   |
|  ```?```      |      any single character   |
| ```[]```      |  a range of characters with "or" relationship |
| ```{}```      |    a list of terms (could be a wildcard) |



### Exercises

1. Before I organized the sequences by gene, what command would have listed all of the sequences of type `.fn`?
2. Before I organized the sequences by gene, what command would have deleted all of sequences belong to geneC?
3. If I want to get information about \_02 version genes how can I do that? 

<br /> 
<br /> 

5.2 Searching (Regular Expression)
----

### Regular Expressions

**A regular expression (shortened as regex) is a sequence of characters that specifies a search pattern in text.**
The ability to search through files and folders can greatly improve your
productivity using Unix. First we'll cover searching through text files.
We are going to work with a list of the names of the states in the US which you
can find at resource folder [here](https://github.com/ginerorama/Introduction-to-Bioinformatic-for-Biologists/tree/main/Resources)). Let's take a look at this file:


```bash
cd ~/bioinformatic_course
ls
```

```
## basckups/
## sequences/
## small.txt
## states.txt
```


```bash
wc states.txt
```

```
## 50      60     472 states.txt
```

It makes sense that there are 50 lines, but it's interesting that there are 60
total words. Let's a take a look at the beginning of the file:


```bash
head states.txt
```

```
## Alabama
## Alaska
## Arizona
## Arkansas
## California
## Colorado
## Connecticut
## Delaware
## Florida
## Georgia
```

This file looks basically how you would expect it to look! For now all you need to know is that text data are
called **strings**. **A string could be a word, a sentence, a book, or a file or 
folder name**. One of the most effective ways to search through strings is to use
**regular expressions**. ***Regular expressions are strings that define patterns
in other strings***. You can use regular expressions to search for a sub-string
contained within a larger string, or to replace one part of a string with
another string.

One of the most popular tools for searching through text files is `grep`. The
simplest use of `grep` requires two arguments: a regular expression and a text
file to search. Let's see a simple example of `grep` in action and then I'll
explain how it works:


```bash
grep "x" states.txt
```

```
## New Mexico
## Texas
```

In the command above, the first argument to `grep` is the regular expression
`"x"`. The `"x"` regular expression represents one instance of the letter "x".
Every line of the `states.txt` file that contains at least one instance of the
letter "x" is printed to the console. As you can see New Mexico and Texas are
the only two state names that contain the letter "x". Let's try searching for 
the letter "q" in all of the state names using `grep`:


```bash
grep "q" states.txt
```

Nothing is printed to the console because the letter "q" isn't in any of the
state names. We can search for more than individual characters though. For
example the following command will search for the state names that contain the
word "New":


```bash
grep "New" states.txt
```

```
## New Hampshire
## New Jersey
## New Mexico
## New York
```

In the previous case the regular expression we used was simply `"New"`, which
represents an occurrence of the string "New". **Regular expressions are not
limited to just being individual characters or words, they can also represent
parts of words**. For example I could search all of the state names that contain
the string "nia" with the following command:


```bash
grep "nia" states.txt
```

```
## California
## Pennsylvania
## Virginia
## West Virginia
```

All of the state names above happen to end with the string "nia".

<br />

### Metacharacters

Regular expressions aren't just limited to searching with characters and
strings, the real power of regular expressions come from using
**metacharacters**. Remember that ***metacharacters are characters that can be used
to represent other characters***. To take full advantage of all of the metacharacters
we should use `grep`'s cousin `egrep`, which just extends `grep`'s capabilities.

<br />

`" . "`

The first metacharacter we should discuss is the `"."` (period) metacharacter, 
which ***represents *any* character***. If for example I wanted to search `states.txt` 
for the character "i", followed by any character, followed by the character "g" 
I could do so with the following command:


```bash
egrep "i.g" states.txt
```

```
## Virginia
## Washington
## West Virginia
## Wyoming
```

The regular expression "i.g" matches the sub-string "irg" in V*irg*inia, and
West V*irg*inia, and it matches the sub-string "ing" in Wash*ing*ton and
Wyom*ing*. The period metacharacter is a stand-in for the "r" in "irg" and the
"n" in "ing" in the example above. The period metacharacter is extremely liberal,
for example the command `egrep "." states.txt` would return every line of
states.txt since the regular expression `"."` would match one occurrence of any
character on every line (there's at least one character on every line). 

<br />

### quantifiers

`quantifiers` are metacharacters which **allow you
to specify the number of times a particular regular expression should appear in 
a string**. 


`" + "`

For example, `"+"` (plus) which represents **one 
or more occurrences of the proceeding expression**. For example the regular 
expression "s+as" means: one or more "s" followed by "as". Let's see if any of 
the state names match this expression:


```bash
egrep "s+as" states.txt
```

```
## Arkansas
## Kansas
```
Both Arkan*sas* and Kan*sas* match the regular expression `"s+as"`. 

<br />

`" * "`


Besides the
plus metacharacter there's also the `"*"` (star) metacharacter which **represents
zero or more occurrences of the preceding expression**. Let's see what happens if
we change `"s+as"` to `"s*as"`:


```bash
egrep "s*as" states.txt
```

```
## Alaska
## Arkansas
## Kansas
## Massachusetts
## Nebraska
## Texas
## Washington
```

As you can see the star metacharacter is much more liberal with respect to
matching since many more state names are matched by `"s*as"`.

<br />

`" {} "`

There are more
specific quantifies you can use beyond "zero or more" or "one or more"
occurrences of an expression. You can use curly brackets (`{ }`) **to specify an
exact number of occurrences of an expression**. For example the regular expression
`"s{2}"` specifies exactly two occurrences of the character "s". Let's try using
this regular expression:


```bash
egrep "s{2}" states.txt
```

```
## Massachusetts
## Mississippi
## Missouri
## Tennessee
```

Take note that the regular expression `"s{2}"` is equivalent to the regular
expression `"ss"`. We could also search for state names that have between two
and three adjacent occurrences of the letter "s" with the regular expression
`"s{2,3}"`:


```bash
egrep "s{2,3}" states.txt
```

```
## Massachusetts
## Mississippi
## Missouri
## Tennessee
```

Of course the results are the same because there aren't any states that have "s"
repeated three times.


`" () "` 

You can use a **capturing group** in order to search for multiple occurrences of
a string. **You can create capturing groups within regular expressions by using
parentheses (`"( )"`)**. For example if I wanted to search states.txt for the
string "iss" occurring twice in a state name I could use a capturing group and
a quantifier like so:


```bash
egrep "(iss){2}" states.txt
```

```
## Mississippi
```

We could combine more quantifiers and capturing groups to dream up even more
complicated regular expressions. For example, the following regular expression
describes three occurrences of an "i" followed by two of any character:


```bash
egrep "(i.{2}){3}" states.txt
```

```
## Mississippi
```

The complex regular expression above still only matches "Mississippi".

### Character Sets

For the next couple of examples we're going to need some text data beyond the
names of the states. Let's just create a short text file from the console:


```bash
touch small.txt
echo "abcdefghijklmnopqrstuvwxyz" >> small.txt
echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" >> small.txt
echo "0123456789" >> small.txt
echo "aa bb cc" >> small.txt
echo "rhythms" >> small.txt
echo "xyz" >> small.txt
echo "abc" >> small.txt
echo "tragedy + time = humor" >> small.txt
echo "http://www.jhsph.edu/" >> small.txt
echo "#%&-=***=-&%#" >> small.txt
```

In addition to quantifiers there are also regular expressions for describing
sets of characters. The `\w` metacharacter corresponds to all "word" characters,
the `\d` metacharacter corresponds to all "number" characters, and the `\s`
metacharacter corresponds to all "space" characters. Let's take a look at using
each of these metacharacters on small.txt:


```bash
egrep "\w" small.txt
```

```
## abcdefghijklmnopqrstuvwxyz
## ABCDEFGHIJKLMNOPQRSTUVWXYZ
## 0123456789
## aa bb cc
## rhythms
## xyz
## abc
## tragedy + time = humor
## http://www.jhsph.edu/
```


```bash
egrep "\d" small.txt
```

```
## 0123456789
```


```bash
egrep "\s" small.txt
```

```
## aa bb cc
## tragedy + time = humor
```

As you can see in the example above, the `\w` metacharacter matches all letters,
numbers, and even the underscore character (`_`). We can see the complement of
this grep by adding the `-v` flag to the command:


```bash
egrep -v "\w" small.txt
```

```
## #%&-=***=-&%#
```

The `-v` flag (which stands for in**v**ert match) makes `grep` return all of the
lines not matched by the regular expression. Note that the character sets for 
regular expressions also have their inverse sets: `\W` for non-words, `\D` for
non-digits, and `\S` for non-spaces. Let's take a look at using `\W`:


```bash
egrep "\W" small.txt
```

```
## aa bb cc
## tragedy + time = humor
## http://www.jhsph.edu/
## #%&-=***=-&%#
```

The returned strings all contain non-word characters. Note the difference between
the results of using the invert flag `-v` versus using an inverse set regular
expression.

In addition to general character sets we can also create specific character
sets using square brackets (`[ ]`) and then including the characters we wish to
match in the square brackets. For example the regular expression for the set
of vowels is `[aeiou]`. You can also create a regular expression for the
complement of a set by including a caret (`^`) in the beginning of a set. For
example the regular expression `[^aeiou]` matches all characters that are not
vowels. Let's test both on small.txt:


```bash
egrep "[aeiou]" small.txt
```

```
## abcdefghijklmnopqrstuvwxyz
## aa bb cc
## abc
## tragedy + time = humor
## http://www.jhsph.edu/
```

Notice that the word "rhythms" does not appear in the result (it's the longest
word without any vowels that I could think of).


```bash
egrep "[^aeiou]" small.txt
```

```
## abcdefghijklmnopqrstuvwxyz
## ABCDEFGHIJKLMNOPQRSTUVWXYZ
## 0123456789
## aa bb cc
## rhythms
## xyz
## abc
## tragedy + time = humor
## http://www.jhsph.edu/
## #%&-=***=-&%#
```

Every line in the file is printed, because every line contains at least one
non-vowel! If you want to specify a range of characters you can use a hyphen
(`-`) inside of the square brackets. For example the regular expression `[e-q]`
matches all of the lowercase letters between "e" and "q" in the alphabet
inclusively. Case matters when you're specifying character sets, so if you
wanted to only match uppercase characters you'd need to use `[E-Q]`. To ignore
the case of your match you could combine the character sets with the `[e-qE-Q]`
regex (short for regular expression), or you could use the `-i` flag with `grep`
to **i**gnore the case. Note that the `-i` flag will work for any provided regular
expression, not just character sets. Let's take a look at some examples using
the regular expressions that we just described:


```bash
egrep "[e-q]" small.txt
```

```
## abcdefghijklmnopqrstuvwxyz
## rhythms
## tragedy + time = humor
## http://www.jhsph.edu/
```


```bash
egrep "[E-Q]" small.txt
```

```
## ABCDEFGHIJKLMNOPQRSTUVWXYZ
```


```bash
egrep "[e-qE-Q]" small.txt
```

```
## abcdefghijklmnopqrstuvwxyz
## ABCDEFGHIJKLMNOPQRSTUVWXYZ
## rhythms
## tragedy + time = humor
## http://www.jhsph.edu/
```

### Escaping, Anchors, Odds, and Ends

One issue you may have thought about during our little exploration of regular
expressions is how to search for certain punctuation marks in text considering
that those same symbols are used as metacharacters! For example, how would you
find a plus sign (`+`) in a line of text since the plus sign is **also** a
metacharacter? The answer is simply using a backslash (`\`) before the plus sign
in a regex, in order to "escape" the metacharacter functionality. Here are a few
examples:


```bash
egrep "\+" small.txt
```

```
## tragedy + time = humor
```


```bash
egrep "\." small.txt
```

```
## http://www.jhsph.edu/
```

There are three more metacharacters that we should discuss, and two of them come
as a pair: the caret (`^`), which represents the start of a line, and the dollar
sign (`$`) which represents the end of line. These "anchor characters" only
match the beginning and ends of lines when coupled with other regular
expressions. For example, going back to looking at states.txt, I could search
for all of the state names that begin with "M" with the following command:


```bash
egrep "^M" states.txt
```

```
## Maine
## Maryland
## Massachusetts
## Michigan
## Minnesota
## Mississippi
## Missouri
## Montana
```

Or we could search for all of the states that end in "s":


```bash
egrep "s$" states.txt
```

```
## Arkansas
## Illinois
## Kansas
## Massachusetts
## Texas
```



Finally, let's talk about the "or" metacharacter (`|`), which is also called the
"pipe" character. This metacharacter allows you to match either the regex on 
the right or on the left side of the pipe. Let's take a look at a small example:


```bash
egrep "North|South" states.txt
```

```
## North Carolina
## North Dakota
## South Carolina
## South Dakota
```

In the example above we're searching for lines of text that contain the words
"North" or "South". You can also use multiple pipe characters to, for example,
search for lines that contain the words for all of the cardinal directions:


```bash
egrep "North|South|East|West" states.txt
```

```
## North Carolina
## North Dakota
## South Carolina
## South Dakota
## West Virginia
```

Just two more notes on `grep`: you can display the line number that a match
occurs on using the `-n` flag:


```bash
egrep -n "t$" states.txt
```

```
## 7:Connecticut
## 45:Vermont
```

And you can also `grep` multiple files at once by providing multiple file
arguments:


```bash
egrep "New" states.txt canada.txt
```

```
## states.txt:New Hampshire
## states.txt:New Jersey
## states.txt:New Mexico
## states.txt:New York
## canada.txt:Newfoundland and Labrador
## canada.txt:New Brunswick
```

You now have the power to do some pretty complicated string searching using
regular expressions! Imagine you wanted to search for all of the state names 
that both begin and end with a vowel. Now you can:


```bash
egrep "^[AEIOU]{1}.+[aeiou]{1}$" states.txt
```

```
## Alabama
## Alaska
## Arizona
## Idaho
## Indiana
## Iowa
## Ohio
## Oklahoma
```

I know there a many metacharacters to keep track of here so below I've included
a table with several of the metacharacters we've discussed in this chapter:

| Metacharacter |               Meaning                |
|--------------:|:-------------------------------------|
|       .       |            Any Character             |
|      \\w      |                A Word                |
|      \\W      |              Not a Word              |
|      \\d      |               A Digit                |
|      \\D      |             Not a Digit              |
|      \\s      |              Whitespace              |
|      \\S      |            Not Whitespace            |
|     [def]     |         A Set of Characters          |
|    [^def]     |           Negation of Set            |
|     [e-q]     |        A Range of Characters         |
|       ^       |         Beginning of String          |
|       $       |            End of String             |
|      \\n      |               Newline                |
|       +       |       One or More of Previous        |
|       *       |       Zero or More of Previous       |
|       ?       |       Zero or One of Previous        |
|    &#124;     | Either the Previous or the Following |
|      {6}      |        Exactly 6 of Previous         |
|    {4, 6}     |     Between 4 and 6 of Previous      |
|     {4, }     |        4 or more of Previous         |

If you want to experiment with writing regular expressions before you use them
I highly recommend playing around with http://regexr.com/.

### find

If you want to find the location of a file or the location of a group of files
you can use the `find` command. This command has a specific structure where
the first argument is the directory where you want to begin the search, and all
directories contained within that directory will also be searched. The first
argument is then followed by a flag that describes the method you want to use to
search. In this case we'll only be searching for a file by its name, so we'll
use the `-name` flag. The `-name` flag itself then takes an argument, the name
of the file that you're looking for. Let's go back to the home directory and
look for some files from there:


```bash
cd
pwd
```

```
## /Users/jgl/
```

Let's start by looking for a file called states.txt:


```bash
find . -name "states.txt"
```

```
## ./bioinformatic_course/states.txt
```

Right where we expected it to be! Now let's try searching for all `.fa` files:


```bash
cd bioinformatic_course
find . -name "*.fa"
```

```
./sequences/geneF_01.fa
./sequences/geneD_01.fa
./sequences/geneB/geneB_01.fa
./sequences/geneB/geneB_02.fa
./sequences/geneE_01.fa
./sequences/geneC_01.fa
./sequences/geneA/geneA_04.fa
./sequences/geneA/geneA_01.fa
./sequences/geneA/geneA_02.fa
./sequences/geneC_03.fa
```

Good file hunting out there!

### Summary

- `grep` and `egrep` can be used along with regular expressions to search for
patterns of text in a file.
- Metacharacters are used in regular expressions to describe patterns of
characters.
- `find` can be used to search for the names of files in a directory.





### Exercises

1. Search `states.txt` for lines that contain the word "New".
2. Make five text files containing the names of states that don't contain one of each of the five vowels.





