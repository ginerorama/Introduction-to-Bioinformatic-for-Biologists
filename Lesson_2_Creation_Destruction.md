Lesson 2: Creation, Destruction and Inspection
==============================================

<br />

2.1 Creating files
---------------------------------------------

There are a few different ways to create a new file on the command line. The most simple way to create a blank file is to use the `touch` command, followed by the path to the file you want to create. In this example we are going to create a new journal entry using touch:


```BASH
touch journal-2017-01-24.txt
ls
## journal-2017-01-24.txt
```

Another easy way to create a file is using **output redirection**. Output redirection stores text that would be normally printed to the command line in a text file. You can use output redirection by typing the greater-than sign` > `at the end of a command followed by the name of the new file that will contain the output from the proceeding command. Let's try an example using echo:

```BASH
$ echo "I'm in the terminal."
## I'm in the terminal.
```
```BASH
echo "I'm in the file." > echo-out.txt
```

Only the first command printed output to the terminal. Let's see if the second command worked:


```BASH
ls
## Desktop
## Documents
## Photos
## Music
## Code
## journal-2017-01-24.txt
## echo-out.txt
```
```BASH
cat echo-out.txt
## I'm in the file.
```

It worked! You can also append text to the end of a file using two greater-than signs `>>`. Let's try this feature out:

```BASH
echo "I have been appended." >> echo-out.txt
cat echo-out.txt
## I'm in the file.
## I have been appended.
```

***Now for a word of warning***. Imagine that you want to append another line to the end of echo-out.txt, so you type echo "A third line." > echo-out.txt into the terminal when really you meant to type echo "A third line." >> echo-out.txt. Let's see what happens:

```BASH
echo "A third line." > echo-out.txt
cat echo-out.txt
## A third line.
```
Unfortunately we have unintentionally overwritten what was already contained in echo-out.txt. There is no undo button in Unix so we will have to live with this mistake. This is the first of several lessons demonstrating the damage that you should try to avoid inflicting with Unix. Make sure to take extra care when executing commands that can modify or delete a file, a typo in the command can be potentially devastating. Thankfully there are a few strategies for protecting yourself from mistakes, including managing permissions for files

<br />

### creating and editing files

Finally we should discuss how to create and edit text files. There are several file editors that are available for your terminal including **vim** and **emacs**. Here the one text editor we will discuss using is called `nano`. It is a very simply text editor that use your entire terminal window. Let's create and edit *todo.txt* using `nano`:

```BASH
nano todo.txt
```
<br />

```
GNU nano 2.0.6                File: todo.txt







^G Get Help   ^O WriteOut   ^R Read File  ^Y Prev Page  ^K Cut Text   ^C Cur Pos
^X Exit       ^J Justify    ^W Where Is   ^V Next Page  ^U UnCut Text ^T To Spell
```
<br />

Once you have started `nano` you can start editing the text file. The top line of the nano editor shows the file you are currently working on, and the bottom two lines show a few commands that you can use in nano. The caret character (`^`) represents the `Control` key on your keyboard, so you can for example type `Control` + `O` in order to save the changes you have made to the text file, or `Control` + `X` in order to exit `nano` and go back to the prompt.


```
GNU nano 2.0.6                File: todo.txt

- email Jaime
- write bioinformatic protocols
- write final section of "R command Line"




^G Get Help   ^O WriteOut   ^R Read File  ^Y Prev Page  ^K Cut Text   ^C Cur Pos
^X Exit       ^J Justify    ^W Where Is   ^V Next Page  ^U UnCut Text ^T To Spell
```
<br />

`nano` is a good editor for beginners because it works similarly to word processors you have used before. You can use the arrow keys in order to move your cursor around the file, and the rest of the keys on your keyboard work as expected. Let's add an item to the to-do list and then we will save and exit `nano` by typing `Control` + `O` followed by `Control` + `X`.


Now let's quickly check if those changes were saved correctly:

```BASH
cat todo.txt
## - email Jaime
## - write bioinformatic protocols
## - write final section of "R command Line"
```

<br />

### Filename conventions

We should note here that a `directory` is merely a special type of `file`. So the rules and conventions for naming files apply also to directories.

1. characters with special meanings such as `/` `*` `&` `%` , should be avoided. 
2. **avoid using spaces within names**. 
3. **use only alphanumeric characters**, that is, letters and numbers, together with `_` (underscore) and `.` (dot).
4. File names conventionally ***start with a lower-case letter***, 
5. File names conventionally end with a (.) followed by a group of letters **indicating the contents of the file**. For example, all files consisting of Python code may be named with the ending `.py`, for example, `myprogram.py`. Then in order to list all files containing Python code in your home directory, you need only type ls `*.py` in that directory.





2.2 Copying Files
-----------------

### cp (copy)

`cp file1 file2` is the command which makes a copy of **file1** in the current working directory and calls it **file2**

What we are going to do now, is to take a file stored in an open access area of the file system, and use the cp command to copy it to your **bioinformatic_course** directory.

First, `cd to your **bioinformatic_course** directory.

    $ cd ~/bioinformatic_course

Then at the UNIX prompt, type,

    $ cp ~/Desktop/science.txt .

(Note: Don't forget the dot (.) at the end. Remember, in UNIX, the dot means the current directory.). The above command means copy the file **science.txt** to the current directory, keeping the name the same. Its the same that this:

	 $ cp ~/Desktop/science.txt /Users/jgl/bioinformatic_course


Be aware that there is one difference between copying files and folders, when copying folders you need to specify the `-r` option, which is short for recursive. This ensures that the underlying directory structure of the directory you wish to copy remains intact. Let's try copying **bioinformatic_course** directory into the **Document** directory:

```BASH
cd ~
cp -r bioinformatic_course  ~/Desktop/bioinformatic_course
cd ~/Desktop/bioinformatic_course
ls
```




### Exercise 2a

Create a backup of your **science.txt** file by copying it to a file called **science.bak**

2.3 Moving files
----------------

### mv (move)

`mv file1 file2` moves (or renames) **file1** to **file2**

To move a file from one place to another, use the `mv` command. This has the effect of moving rather than copying the file, so you end up with only one file rather than two.

It can also be used to rename a file, by moving the file to the same directory, but giving it a different name.

We are now going to move the file science.bak to your backup directory.

First, change directories to your unixstuff directory (can you remember how?). Then, inside the **bioinformatic_course** directory, type

```BASH
$ mv science.bak backups/.
```

Type `ls` and `ls backups` to see if it has worked.


2.4 Removing files and directories
----------------------------------

### rm (remove), rmdir (remove directory)

To delete (remove) a file, use the `rm` command. As an example, we are going to create a copy of the **science.txt** file then delete it.

Inside your **bioinformatic_course** directory, type

```BASH
$ cp science.txt tempfile.txt  
$ ls (to check if it has created the file)  
$ rm tempfile.txt  
$ ls (to check if it has deleted the file)
```

You can use the `rmdir` command to remove an empty directory (make sure it is empty first) or `rm -r` (for recursively remove all the files and folders inside the directory). Try to remove the **backups** directory. You will not be able to since UNIX will not let you remove a non-empty directory.

### Exercise 2b

1. Create a directory called **tempstuff** using mkdir, then remove it using the `rmdir` command.
2. Remove the bioinformatic_course folder that we copied at the Desktop 

2.5 Displaying the contents of a file on the screen
---------------------------------------------------


### cat (concatenate)

The command `cat` can be used to display the contents of a file on the screen. Type:

```BASH
cat science.txt
```

As you can see, the file is longer than than the size of the window, so it scrolls past making it unreadable.

### less

The command `less` writes the contents of a file onto the screen a page at a time. Type


```BASH
less science.txt
```

Press the `[space-bar]` if you want to see another page, type `[q]` if you want to quit reading. As you can see, less is used in preference to cat for long files.

### head

The `head` command writes the first ten lines of a file to the screen.

First clear the screen then type

```BASH       
head science.txt
```
![](2.5.png)

Then type

```BASH
head -5 science.txt
```


What difference did the -5 do to the head command?

### tail

The `tail` command writes the last ten lines of a file to the screen.

Clear the screen and type

```BASH
tail science.txt
```

![](2.6.png)

How can you view the last 15 lines of the file?

2.6 Searching the contents of a file
------------------------------------

### Simple searching using less

Using `less`, you can search though a text file for a keyword (pattern). For example, to search through **science.txt** for the word 'science', type

```BASH
less science.txt
```
  
then, still in less (i.e. don't press \[q\] to quit), type a forward slash `[/]` followed by the word to search

`/science`

As you can see, less finds and highlights the keyword. Type `[n]` to search for the next occurrence of the word.

### grep 

grep is one of many standard UNIX utilities. It searches files for specified words or patterns. First clear the screen, then type


```BASH
$ grep science science.txt
```


![](2.2.png)


As you can see, grep has printed out each line containg the word science.

Or has it????

Try typing

    $ grep Science science.txt
    
![](2.3.png)
    

The grep command is **case sensitive**; it distinguishes between Science and science.

To ignore upper/lower case distinctions, use the **\-i option**, i.e. type

    $ grep -i science science.txt


![](2.4.png)

To search for a phrase or pattern, you must enclose it in single quotes (the apostrophe symbol). For example to search for spinning top, type

    $ grep -i 'spinning top' science.txt

Some of the other options of grep are:

**\-v** display those lines that do NOT match  
**\-n** precede each maching line with the line number  
**\-c** print only the total count of matched lines  

Try some of them and see the different results. Don't forget, you can use more than one option at a time, for example, *the number of lines without the words science or Science is*

    $ grep -ivc science science.txt

### wc (word count)

A handy little utility is the `wc` command, short for word count. To do a line/word/character count on **science.txt**, type

    $ wc science.txt
    
The result show three diferent numbers in a row, the number of lines, words and characters followed by the file name.

![](2.1.png)


If you only want to get the number of lines

	$ wc -l science.txt

<br />
    
    
 2.7 Wildcards
---------------------------------------------

### The characters `*` and `?`

The character `*` is called a wildcard, and will match against none or more character(s) in a file (or directory) name. For example, in your **bioinformatic_course** directory, type

```
$ touch list1 list22 list33 1list
```
This line will create three files named list1 list2 list3, we will see in next chapter what touch command exactly do. Now we will take advantage of `*` characters to find all list files, type

`$ ls list*`

This will list all files in the current directory starting with list....

Try typing

`$ ls *list`

This will list all files in the current directory ending with ....list

The character `?` will match exactly one character.
So `ls ?ouse` will match files like house and mouse, but not grouse.
Try typing

`$ ls ?list`   
    
Finally we can use also wildcards to remove a series of files that share some characters, type `rm list*` to remove list1 list2 and list3 files.





Summary
-------

command | function|
------- | ---------------|
`touch`| creates empty files|
`>`| You can use > to redirect the output of a command into a file|
`>>` |will append command output to the end of a file|
`nano file.tx` | create and edit a file with this  simple text editor|
`cp file1 file2`| copy file1 and call it file2|
`mv file1 file2`| move or rename file1 to file2|
`rm file`| remove a file|
`rmdir directory` | remove a directory|
`rm -r directory`| remove recursively|
`cat file`| display a file|
`more file`| display a file a page at a time|
`head file`| display the first few lines of a file|
`tail file`| display the last few lines of a file|
`grep 'keyword' file`| search a file for keywords|
`wc file`| count number of lines/words/characters in file|
`*`| its a wildcard that match against one or more characters
`?`| its a wildcard that match exactly one character

### Exercises

1. Create a file called `message.txt` in your home directory and move it into another directory.
1. Copy the `message.txt` you just moved into your home directory.
1. Create a new directory called `workbench` in your home directory.
1. Without changing directories create a file called `readme.txt` inside of `workbench`.
1. Append the numbers 1, 2, and 3 to `readme.txt` so that each number appears on it's own line.
1. Print `readme.txt` to the command line.
1. Use output redirection to create a new file in the `workbench` directory called `list.txt` which lists the files and folders in your home directory.
1. Find out how many characters and lines are in `list.txt` without opening the file or printing it to the command line.
1. Print the first and the last line of `list.txt` in the command line.

### Excercise II
1. Download the file sequences.fasta present in the resources folder of this repository
2. Print the header of the first fasta sequence
3. Print the header of the last fasta sequence
4. How many Proteins sequences contain sequences.fasta ?.
5. How many secuences contains the motif LLR
6. Try -B1 option to have a look the name of the sequences that contains the LLR motif. All the sequences contains the same number of motif?
7. Using nano modify the header of the first fasta sequence, remove all words after the tr|A0A060IHA6|A0A060IHA6_9RHIZ ID
