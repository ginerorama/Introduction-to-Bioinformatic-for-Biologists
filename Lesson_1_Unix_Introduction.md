UNIX Introduction 1
===================




1.1 The Linux Terminal
---------------------------------

The Linux terminal is a text-based interface used to control a Linux computer. It's just one of the many tools provided to Linux users for accomplishing any given task, but it's widely considered the most efficient method available.

### the shell

In a Linux system, the shell is a command-line interface that interprets a user’s commands and script files, and tells the operating system what to do with them. There are several shells that are widely used, such as the Bourne-Again shell `(bash)` and Z shell `(zsh)`. Each shell has its own feature set and intricacies regarding how commands are interpreted, but they all feature input and output redirection, variables, and condition-testing, among other things.


When you first login to a server, you will typically be greeted by the Message of the Day (MOTD), which is typically an informational message that includes miscellaneous information such as the version of the Linux distribution that the server is running. After the MOTD, you will be dropped into the command prompt, or shell prompt, which is where you can issue commands to the server.

The information that is presented at the command prompt can be customized by the user, but here is an example of the default Ubuntu 18.00 command prompt:


<p align="center">
<img src="/media/lesson_1/9.png" alt="drawing"/>
</p>



Here is a breakdown of the composition of the ***command prompt***:

***mark***: The username of the current user

***linux-desktop***: The computer name (or the hostname of the server)

***~***: The current directory. In bash, which is the default shell, the ~, or tilde, is a special character that expands to the path of the current user’s home directory; in this case, it represents /home/mark

***$***: The prompt symbol. This denotes the end of the command prompt, after which the user’s keyboard input will appear $


### Running Commands 

The prompt is just there to let you know that the shell is ready for you to type in a command. Press `Enter` on your keyboard a few times to see what happens with the prompt. Your shell should now look like this:



<p align="center">
<img src="/media/lesson_1/11.png" alt="drawing" />
</p>



If you don't type anything after the prompt and you press `Enter` then nothing
happens and you get a new prompt under the old prompt. The white rectangle 
after the prompt is just a cursor that allows you to edit what you have typed
into the shell. Your cursor might look like a rectangle, a line, or an
underscore, but all cursors behave the same way. After typing something into
the command line you can move the cursor back and forth with the left and right
arrow keys, just like you would when typing an email.

Now that we have pressed `Enter` several times our shell looks messy with all of 
those old prompts! Do not worry, you are about to learn your first shell command 
which will clear all of those old prompts from your shell. Type `clear` at the 
prompt and then hit `Enter`. Voila! Your shell now only has the current prompt,
just like when you first opened the terminal.

Every command line command is actually a little computer program (which can be a **binary** program or a **script**), even commands
as simple as `clear` or `date`. This last allow to retrive the current date in the terminal:



<p align="center">
<img src="/media/lesson_1/10.png" alt="drawing"/>
</p>

These commands all tend to have the following structure:

```
[command] [options] [arguments]
```

Some simple commands like `clear` or `date` do not require any options or arguments.

<br />

**Options** are usually preceded by a hyphen (`-`) and they tweak the behavior
of the command. <br />


**Arguments** can be names of files, raw data, or other options
that the command requires. <br />


A simple command that has an argument is `echo`.
The `echo` command prints a phrase to the console. Enter `echo 'Hello World!'`
into the command line to see what happens:
<br />

```bash
echo 'Hello World!'
```

```
## Hello World!
```


You can use `echo` to print any phrase surrounded by single
quotes (`''`) to the console.

If you want to see the last command press the `Up` arrow key. You can press
`Up` and `Down` in order to scroll through the history of commands that you've
entered. If you want to re-execute a past command, you can scroll to that
command then press `Enter`. Try getting back to the `echo 'Hello World!'`
command and execute it again.


### Process and case-sensitive

An instance of a running command is known as a **process**. When a command is executed in the **foreground**, which is the default way that commands are executed, the user must wait for the process to finish before being returned to the command prompt, at which point they can continue issuing more commands.

It is important to note that almost ***everything in Linux is case-sensitive***, including file and directory names, commands, arguments, and options. If something is not working as expected, double-check the spelling and case of your commands!



### Exercises

1. Print your name to the terminal.
2. Clear your terminal after completing #1.



1.2 Listing files and directories
---------------------------------

### ls (list)

When you first login, your current working directory is your home directory. Your home directory has the same name as your user-name, in my case, **jgl**, and it is where your personal files and subdirectories are saved.

<p align="center">
<img src="/media/lesson_1/1.png" alt="drawing" "/>
</p>

To find out what is in your home directory, type

`$ ls (short for list)`

<p align="center">
<img src="/media/lesson_1/2.png" alt="drawing" "/>
</p>

The `ls command lists the contents of your current working directory, but only the names of files and directories. 

To get a more detailed information about the files and directories, type


`$ ls -l (long format)`


<p align="center">
<img src="/media/lesson_1/3.png" alt="drawing" "/>
</p>

We can observe now a lot of information distributed by columns for all the files and directories:

columns | Information	  |
------- | ---------------|
1       | File permissions ('d' means is a directory)|  
3       | Owner|
4       | Group|
5       | Size (bytes)-meaningful for files, but not for directories.|  
6, 7 and 8| Last modification time |


`ls` is an example of a command which can take options: `-l` is an example of an option. The options change the behaviour of the command. There is a system manual that tell you which options a particular command can take, and how each option modifies the behaviour of the command, for that we can use the command *man*:

`$ man ls`





Try now to use `-h` to display unit suffixes in column 5 for file sizes: Byte, Kilobyte, Megabyte...

<p align="center">
<img src="/media/lesson_1/4.png" alt="drawing" />
</p>


`ls` does not, in fact, print all the files/directories in your home directory to be listed, but only those ones whose name does not begin with a dot (**.**) Files beginning with a dot (**.**) are known as hidden files and usually contain important program configuration information. They are hidden because you should not change them unless you are very familiar with UNIX!!!

To list all files and directories in your home directory including those whose names begin with a dot, type:

`$ ls -la`

<p align="center">
<img src="/media/lesson_1/5.png" alt="drawing" />
</p>

<br />

### Linux directory structure

Linux is based on UNIX and hence it borrows its filesystem hierarchy from UNIX. You’ll fine a similar directory structure in UNIX-like operating systems such as Ubuntu and macOS. I’ll be using the term Linux hereafter instead of UNIX though.

### / – The root directory
Everything, all the files and directories, in Linux are located under `root` represented by `/`. If you look at the directory structure, you’ll realize that it is similar to a plant’s root.


<p align="center">
<img src="/media/lesson_1/UnixDirectoryTree.png" alt="drawing" />
</p>

Since all other directories or files are descended from root, the absolute path of any file is traversed through root. For example, if you have a file in /home/jelkner/pubic_html, you can guess that the directory structure goes from root->home->jelkner->public-html->index.html.

 <br />

1.3 Making Directories
----------------------

### mkdir (make directory)

We will now make a subdirectory in your home directory to hold the files you will be creating and using in the course of this tutorial. To make a subdirectory called unixstuff in your current working directory type:

`$ mkdir bioinformatic_course`

To see the directory you have just created, type:

`$ ls`

 <br />


1.4 Changing to a different directory 
--------------------------------------

### cd (change directory)

The command cd directory means change the current working directory to 'directory'. The current working directory may be thought of as the directory you are in, i.e. your current position in the file-system tree.

To change to the directory you have just made, type:

`$ cd bioinformatic_course`

Type `ls` to see the contents (which should be empty)

 <br />


### Exercises

Make another directory inside the **bioinformatic_course** directory called **backups**


 <br />


1.5 The directories . and ..
----------------------------

Still in the **bioinformatic_course/** directory, type

`$ ls -la`

<p align="center">
<img src="/media/lesson_1/6.png" alt="drawing" />
</p>


As you can see, in the **bioinformatic_course/** directory (and in all other directories), there are two special directories called (**.**) and (**..**)

In UNIX, (**.**) means the current directory, so typing

`$ cd .`

*NOTE*: there is a space between cd and the dot

means stay where you are (the **bioinformatic_course/** directory).

This may not seem very useful at first, but using (**.**) as the name of the current directory will save a lot of typing, as we shall see later in the tutorial.

(**..**) means the parent of the current directory, so typing

`$ cd ..`

will take you one directory up the hierarchy (back to your home directory). *Try it now*.

*Note:* typing `cd` with no argument always returns you to your home directory. This is very useful if you are lost in the file system.


 <br />


1.6 Pathnames
-------------


### pwd (print working directory)

Pathnames enable you to work out where you are in relation to the whole file-system. For example, to find out the absolute pathname of your home-directory, type `cd` to get back to your home-directory and then type

`$ pwd`

The full pathname will look something like this -

**/Users/jgl**

<p align="center">
<img src="/media/lesson_1/7.png" alt="drawing" />
</p>


which means that **jgl** (your home directory) is in the directory **Users** (the group directory),which is located on the **root** "/".


### absolute and relative paths


The *Absolute path* always starts from the root directory (/). For example, 

> `/Users/jgl/bioinformatic_course/backups`


A *relative path* starts from the current directory. For example, if you are in the **/User** directory and you want to access the my_scripts.sh file stored in backups, you can use jgl/bioinformatic_course/backups/my_scripts.sh.


### Understanding the difference between absolute and relative paths

You know that the directory structure in Linux resembles the root of a tree. Everything starts at root and branches out from there.

Now imagine that you are in the directory `abhishek/` and you want to access `my_scripts.sh` file.

The *absolute path* is depicted in the green dotted line and the relative path is depicted in the yellow dotted lines


<p align="center">
<img src="/media/lesson_1/8.png" alt="drawing" />
</p>



Suppose you want to see the properties of the file my_script.sh using the `ls` command.

You may use the *absolute path* that starts with the root directory (/):

`ls -l /home/abhishek/scripts/my_script.sh`

Or, you can use the *relative path* (which starts from the current directory, not /):

`ls -l scripts/my_script.sh`

Both commands will yield the same result (except for the path of the file).




### Exercise

Use the commands **ls**, **pwd** and **cd** to explore the file system.

(Remember, if you get lost, type cd by itself to return to your home-directory)

Create another directory in bioinformatic_course named `scripts`, and inside of `scripts` create again a new directory named `python`. Now retrieve the relative path of `backups/` folder from your current directory `python/`. Retrieve also the absolute path of `Python/` directory

Try to use the command ***tree***: go to your home directory and type `tree Course`
(if tree does not work, you will have to install it. type `sudo apt-get install tree`)

<br />

1.7 More about home directories and pathnames
---------------------------------------------

### Understanding pathnames

First type `cd` to get back to your home-directory, then type

`$ ls bioinformatic_course`

to list the conents of your **bioinformatic_course** directory.

Now type

`$ ls backups`

You will get a message like this -

> backups: No such file or directory

The reason is, **backups** is not in your working directory (the directory you are currently in). To use a command on a file (or directory) not in the working directory, you must either cd to the correct directory, or specify its `full pathname`. To list the contents of your backups directory, you must type

`$ ls bioinformatic_course/backups`


### ~ (your home directory)

Home directories can also be referred to by the tilde **~** character. It can be used to specify paths starting at your home directory. So typing

    `$ ls ~/bioinformatic_course`

will list the contents of your **bioinformatic_course** directory, no matter where you currently are in the file system.

What do you think `$ ls ~` would list?

What do you think `$ ls ~/.` would list?



### SUMMARY

command | function|
------- | ---------------|
ls | list files and directories|
ls -l | list files/directories in long format|
ls -lh| list in long format with suffixes for files size|
ls -a|	list all (include hide) files and directories|
mkdir|	make a directory|
cd directory|	change to named directory|
cd|	change to home-directory|
cd ~|	change to home-directory|
cd ..|	change to parent directory|
pwd|	display the path of the current directory|
