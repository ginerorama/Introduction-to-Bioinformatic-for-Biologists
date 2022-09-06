

UNIX 3: process control 
===================

3.1 Redirection  
-----------------

Most processes initiated by UNIX commands write to the **standard output** (that is, they write to the terminal screen), and many take their input from the **standard input** (that is, they read it from the keyboard). There is also the **standard error**, where processes write their error messages, by default, to the terminal screen.


![](stdin_3_1.png)

Under Linux there are three standard streams:

1. **Standard input** -> channel (0) where programs receive their data, mostly this is the keyboard (unless redirected)
1. **Standard output** -> channel (1) where programs print there outcome, by default this is the terminal window
1. **Standard error** -> channel (2) where programs write output messages, by default this is the terminal window

We have already seen one use of the cat command to write the contents of a file to the screen.

Now type cat without specifing a file to read

    $ cat

Then type a few words on the keyboard and press the `[Return]` key.

Finally hold the `[Ctrl]` key down and press `[d]` (written as ^D for short) to end the input (EOF).

What has happened?

If you run the cat command without specifing a file to read, it reads the standard input (the keyboard), and on receiving the'end of file ' (**EOF**), copies it to the standard output (the screen).

In UNIX, we can redirect both the input and the output of commands.

3.2 Redirecting the Output  
----------------------------
Most UNIX programs print the output on the standard output(the terminal). To redirect the output to a file or create a new file you can use  `>` ,` 1>` or `>>`


`$ > file1.txt` a new file is created, existing file is overwritten with output from the command

`$ >> file1.txt` a new file is created if it does not exist. Otherwise, the output is appended at the end of
the existing file


We use the `>` symbol to redirect the output of a command (including stderr). For example, to create a file called **list1** containing a list of fruit, type  

    $ cat > list1

Then type in the names of some fruit. Press `[Return]` after each one.

pear  
banana  
apple  
^D (Control D to stop, EOF)

What happens is the cat command reads the **standard input** (the keyboard) and the `> `redirects the **output**, which normally goes to the screen, into a file called **list1**

To read the contents of the file, type

    $ cat list1
    
    
![](3_2.png)

    

### Exercise 3a

Using the above method, create another file called **list2** containing the following fruit: orange, plum, mango, grapefruit. Read the contents of **list2**

----------

The form `>>` appends standard output to a file. So to add more items to the file **list1**, type

    $ cat >> list1

Then type in the names of more fruit

peach  
grape  
orange  
^D (EOF)

To read the contents of the file, type

    $ cat list1

![](3_3.png)

You should now have two files. One contains six fruit, the other contains four fruit. We will now use the cat command to join (concatenate) **list1** and **list2** into a new file called **biglist**. Type

    $ cat list1 list2 > biglist

What this is doing is reading the contents of **list1** and **list2** in turn, then outputing the text to the file **biglist**

To read the contents of the new file, type

    $ cat biglist
    
![](3_4.png)
    

### Redirecting the error

Sometimes a commands outputs some warnings and errors on the screen. This is not ***standard output*** but ***standard error*** (channel 2). In the same way you redirect channel 1 to a file, you can
export channel 2 to a ‘error.txt’ file.

    $ lsp 2> error.txt
    $ cat error.txt
 
 
Sometimes we are no interested in the error message from channel 2 at all and directly we sending the message to 'bit-heaven' instead of save it in a file
 
   $ lsp 2>/dev/null
 

3.3 Redirecting the Input  
---------------------------

Some commands take their input from the keyboard (standard input stream), but this can be modified. The **input** can be received from a file for example. To redirect the input of a command, use `<` or `0<` proceeded by the location/name of that file or directly the location/name of the file


    $ cat 0< list1
    $ cat < list1
    $ cat list1



The command `sort` alphabetically or numerically sorts a list. Type

    $ sort


Then type in the names of some vegetables. Press `[Return]` after each one.

carrot  
beetroot  
artichoke  
^D (EOF)  

The output will be

artichoke  
beetroot  
carrot

Now using `<` you can redirect the input to come from a file rather than the keyboard. For example, to sort the list of fruit, type

    $ sort < biglist

and the sorted list will be output to the screen.

To output the sorted list to a file, type,

    $ sort < biglist > slist

Use `cat` to read the contents of the file **slist**


![](3_5.png)

3.4 Pipes
---------

We are able to retrieve the input from a file and redirect the output to another file. Sometimes we just want to redirect the output from one command directly to the input of another without creating a temporary file(s). Then we can use the pipe `|`


Imagine you want the 5 first fruits presented in list1 sorted, and stored in a file named list5sorted 


One method to get a sorted list of the first 5 fruits is to type,

    $ head -n 5 list1 > list5  
    $ sort list5 > list5sorted

This is a bit slow and you have to remember to remove the temporary file called names when you have finished. What you really want to do is connect the output of the who command directly to the input of the sort command. This is exactly what pipes do. The symbol for a pipe is the vertical bar `|`

For example, typing

    $ head -n 5 list1 | sort > list5sorted
    $ cat list5sorted
    
 ![](3_6.png)
 
    

will give the same result as above, but quicker and cleaner.

To check the total number of fruit names presented in list1 you can simply type

    $ cat list1 | wc -l  

### Exercise 3b


Using pipes, print all lines of **list1** and **list2** containing the letter 'p', sort the result, and save in a file named exercise3b

3.4 Multitasking with commands
------------------------------
When using the command line, you can run multiple commands in one line. The commands are then separated by `;`


`wget http://eggnog5.embl.de/download/eggnog_5.0/e5.taxid_info.tsv ; grep Streptococcus e5.taxid_info.tsv | wc -l ` 

Here, just in one line and using the command `wget` you will download the file *e5.taxid_info.tsv* that contains all the taxa presented in Eggnog5 database and find all the entries that belong to genus Streptococcus. 

### Other command separators

* `&&` only execute the command if the preceding one finished correctly

        $ cat e5.taxid_info.tsv | sort > temp && mv temp e5.taxid_info.tsv


* `||` only execute the command if the preceding one didn’t finish correctly (= plan B)

        $ ls -h || cat list1

       now try ls with an incorrect option and see what happen

        $ ls -X || cat list1

       ¿how can we remove the error message from ls -X command?


        $ ls -X 2>/dev/null || cat list1




Summary
-------

command | function|
------- | ---------------|
`command > file`| redirect standard output (channels 1 and 2) to a file| 
`command 1> file`| redirect standard output (only channel 1) to a file| 
`command >> file`| append standard output to a file|
`command 2> error_file` |redirect standard error (2) to a file|
`command < file` | redirect standard input from a file|
`command1 | command2` | pipe the output of command1 to the input of command2|
`command1 ; command2` | concatenate different commands in one line|
`command1 && command2` |execute the command if the preceding one finished correctly|
`command1 || command2` |execute the command if the preceding one didn’t finish correctly|
`cat file1 file2 > file0`| concatenate file1 and file2 to file0
`sort`| sort data

