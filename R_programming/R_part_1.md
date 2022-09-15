R - A brief introduction
------------------------

R is a programming language and free software environment
(<a href="https://www.r-project.org/about.html" class="uri">https://www.r-project.org/about.html</a>).
R, compared with other languages like Python or Ruby, is more oriented
to table manipulation and data analysis.

To introduce R language, R is case-sensitive (it is not the same
Rsubread than rsubread), and normally in a script, \# is used to comment
the lines. In addition, R admits into the variable characters (‘abc’),
numbers (1) or booleans (TRUE/FALSE).

In order to use R, you can use the IDE terminal by clicking on the icon
(if Windows) or typing ‘R’ in a Linux terminal. However, the best way to
start using R is RStudio, an interactive workspace to better understand
the data structure, visualize plots and write code (see more at
<a href="https://rstudio.com" class="uri">https://rstudio.com</a>) in R.
Furthermore, R has an interactive markdown (like a notebook), called
Rmarkdown, becoming very useful in data analysis to show, visualize and
comment data. You can also find two different parts in the markdown: the
description part (in black) and the code part (in grey, flanked by
`{r}`) (colours are orientative, it depends on the appearance. If you do
not feel comfortable with the white environment, you can choose another
appearance in Tools/Global options…/Appearance). RStudio also allow to
connect to Git platforms, enhancing the remote work and the share of
code in the community.

Starting with R language, R is composed by a console (see at the
bottom-left of RStudio), where the code will run into the R terminal. In
Rmarkdown, to run a box with code, just press Ctrl + Enter.

R uses variables to work. An example of a variable is a chain of
characters, like a word. For example, a possible variable could be the
word hello. If the variable is not defined, R console will show an
error: Error: object ‘hello’ not found. To name a variable in R, an
example of the structure is: hello &lt;- 1 (however, you can use also
“=” by “&lt;-”, but it is preferable to use “&lt;-”). If the naming of
the variable is a character array, all characters may be flanked by "“,
for example: hello &lt;-”Hello World!". Once you name a variable, the
variable will be appear in your list of variables at the top-right box,
and you can check by clicking on the variable what is the variable.

Another important part of R is the use of functions to deal with the
variables. A general structure of a function is: function(variable),
where “function” is the name of the function, and the parenthesis
content is the variable to be processed. If you have any doubt about the
function, please run: ?function. For example, an important function in R
is print(). So, if you want to get information, it would be: ?print.

R is structured in a source code and libraries with specific functions
into them. This libraries are also called packages. Some packages are
installed as R core, and specific packages are available in CRAN
repository and Bioconductor. When CRAN repository is more oriented to
base and general packages, Bioconductor is more focused in packages to
process biological data, such as genomic, transcriptomics, metabolomics,
e.g. However, bioconductor is an istaller packages that allow to adapt
biological packages to R environment. Once the package is installed in
R, you can work with their functions by their load into the environment:
library(nameofthelibrary). Sometimes, different libraries contain a
function called the same, so you can avoid possible interferences using
the name of the function like that: dplyr::select(). It means that you
want to use the function select from the dplyr package (very useful in
package building)

To install a general package in R:

    install.packages('dplyr', repos="http://cran.us.r-project.org")  ##Install packages

    ## Installing package into 'C:/Users/David/Documents/R/win-library/4.0'
    ## (as 'lib' is unspecified)

    ## also installing the dependency 'vctrs'

    ## 
    ##   There is a binary version available but the source version is later:
    ##       binary source needs_compilation
    ## dplyr  1.0.8 1.0.10              TRUE
    ## 
    ##   Binaries will be installed
    ## package 'vctrs' successfully unpacked and MD5 sums checked

    ## Warning: cannot remove prior installation of package 'vctrs'

    ## Warning in file.copy(savedcopy, lib, recursive = TRUE): problema al copiar C:
    ## \Users\David\Documents\R\win-library\4.0\00LOCK\vctrs\libs\x64\vctrs.dll a C:
    ## \Users\David\Documents\R\win-library\4.0\vctrs\libs\x64\vctrs.dll: Permission
    ## denied

    ## Warning: restored 'vctrs'

    ## package 'dplyr' successfully unpacked and MD5 sums checked

    ## Warning: cannot remove prior installation of package 'dplyr'

    ## Warning in file.copy(savedcopy, lib, recursive = TRUE): problema al copiar C:
    ## \Users\David\Documents\R\win-library\4.0\00LOCK\dplyr\libs\x64\dplyr.dll a C:
    ## \Users\David\Documents\R\win-library\4.0\dplyr\libs\x64\dplyr.dll: Permission
    ## denied

    ## Warning: restored 'dplyr'

    ## 
    ## The downloaded binary packages are in
    ##  C:\Users\David\AppData\Local\Temp\Rtmp0YZ6w2\downloaded_packages

    library(dplyr)

    ## Warning: package 'dplyr' was built under R version 4.0.5

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

Operators
---------

When you are working with R, you often have to add or multiply some
variables, it is a quotidian action in programming. For that, the
following operators will be used in your programming activity. The
arithmetic operators are:

    x <- 1
    y <- 3
    x + 1 ## summation

    ## [1] 2

    12 - y ##subtraction

    ## [1] 9

    y * x ##multiplication

    ## [1] 3

    4 / 2 ## division

    ## [1] 2

    2 ^ 10 ##powering

    ## [1] 1024

Tips: Please be sure that your named variables are all numeric when use
these arithmetic operators. Sometimes you could have problems in
comparisons by the use of numbers considered by characters arrays, and
the program would show you an error. If it happens and you have a string
array and you want to use arithmetic operators, please use the function
to transform the string array which contain the numbers to be used into
numeric arrays by: x &lt;- as.numeric(x) If your are not sure about the
type of the variable (numeric, character, logical, NA, e.g.), you can
check the nature of the variable by the function: type(variable)

R provides us different possibilities to compare variables or to check
if is true a sentence in a script. Like that, this comparisons are very
useful to check the value of a variable. The comparison operators are:

    x <- 1 ###name a variable
    y <- x+1


    x == x ##Exactly the same (TRUE)

    ## [1] TRUE

    x != y ##Different (! means not, in that case, != not equal) (FALSE)

    ## [1] TRUE

    x < 1  ##Smaller than (FALSE)

    ## [1] FALSE

    x > 3  ##Greater than (FALSE)

    ## [1] FALSE

    y <= 2 ##Smaller or equal than (FALSE)

    ## [1] TRUE

You can use the comparison operators in numeric, string and logical
variables too. However, some limitations could appear because of the
nature of the comparisons (for example, the use of character arrays
cannot be compared with &gt; or &lt; in character arrays by the nature
of the comparisons).

    x <- 'Hello'
    y <- 'Bye'

    x == y ## FALSE

    ## [1] FALSE

    x != y ## TRUE

    ## [1] TRUE

You can also use more than one comparison in your sentence by the use of
| or & . For example:

    x <- 2
    y <- 4

    x <= y & x > 3 ## In this comparison, the use of & (AND) implies that the both sentences must be true. If not, the result will be FALSE.

    ## [1] FALSE

    x <= y | x > 3 ## In this case, the use of | (OR) implies that, at least, one of the comparisons must be true.

    ## [1] TRUE

Data structures
---------------

Following the progress in R knowledge, normally the data is stored in
different structures. The variables can be considered as a single data
(for example, x &lt;- 1) or more complex data. In that case, R allows us
to contain different classes of data structures.

Vectors

One of the structures is the vector structure. Because of the nature of
the data, it is the basic data structure, and we can also include single
data as a vector with length=1 (just one data). In the vectors, all the
data must be composed with the same type (for example, if you want to
create a numeric vector, all components must be numbers. In the case of
a character vectors and this vector includes numbers, the numbers will
be considered as characters, not numbers). To create a vector, you can
create it by:

    x <- c(1, 'sep', 3, 'today') ## c() is combine: build a vector with the content of the parenthesis ****Please be sure that you use comma to separe each element of the vector
    class(x)

    ## [1] "character"

    y <- c(1:6) ## you can create a sequence from 1 to 6 by the use of :
    z <- seq(from=100, by=3, length=5) ## Furthermore, you can create a sequence of numbers by a desired number by seq (you can also set the length of the vector) 

    u <- rep(1:2, 3) ## You can create a vector by a pattern repetition, specifying too the length of the vector by the number of repetitions of the sequences

YOu can also work in arithmetic operations with vectors (numeric
vectors). When one operand is shorter than the other, the shortest one
is recycled, i. e. the vaules from the shorter vector are re-used in
order to have the same length as the longest vector. If one of the
vectors is recycled, a warning is printed in the R console. (Warning is
not an error, the operation will be finished).

    1:3 + 10:12

    ## [1] 11 13 15

In R, you can also subset the vectors to extract some information of a
vector. It is a powerful feature in R, and it allows us to filter data,
re-order data or maybe remove some problematic points.

    alphabet <- LETTERS ## Letters is a built-in vector with the 26 letters of the english alphabet
    alphabet[c(3,15,12,15,21,18, 19)] ## The resulted letters are selected by their specific position in alphabet vector

    ## [1] "C" "O" "L" "O" "U" "R" "S"

    alphabet[15:18] ## the resulted letters are selected from one position to the other position

    ## [1] "O" "P" "Q" "R"

    alphabet[-(15:18)] ## you can also exclude the selected data from the general vector by the use of - . It is very useful in data cleaning when you have outliers in your data.

    ##  [1] "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "S" "T" "U" "V" "W"
    ## [20] "X" "Y" "Z"

    alphabet[-c(5,7,9)]

    ##  [1] "A" "B" "C" "D" "F" "H" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V"
    ## [20] "W" "X" "Y" "Z"

Matrices

Matrices are two dimensional vectors (called tables too), explicitly
created with the matrix function. Just like one dimensional vectors,
they store same-type elements.

    my.matrix <- matrix (1:12, nrow=3, byrow=TRUE) #Creation of a matrix by the use of matrix function. If byrow=FALSE, the serie will be built by column
    dim (my.matrix) ## Check the matrix dimensions 

    ## [1] 3 4

In addition, R allows to subset and indexing matrix by the same bracket
structure than the vector subset. However, vectors have only one
dimension structure, and matrix have two dimensions. For that, the
brackets will contain two dimensions, following the structure:
matrix\[rows,columns\] . For example:

    my.matrix[1,3] ##In this expression, we extract the data from the position row=1, column=3

    ## [1] 3

    my.matrix[,3] ##We can subset by the absence of row specifications all the column

    ## [1]  3  7 11

    my.matrix[3,] ##We can also subset by the same way the rows

    ## [1]  9 10 11 12

Data Frames

Data frames is one of the most important data structure in R. It is a
flexible way to store data and create large datasets with different type
of data (in a same data frame, you can have numeric arrays, string
arrays, logical arrays). In a data frame, usually the observations are
the rows and the variables are the column. For that, each column would
be like a vector (it means that all data contained in the column must be
in the same type), but each column can become with different types
(column 1: num; column 2: str).

    df <- data.frame(type=rep(c('case', 'control'),c(2,3)), time=rnorm(5)) ##In this line, we want to create a data.frame with two columns or variables (column 1: type; column 2: control), where in type column we will create a column with 2 'case' rows or observations and three 'control' rows or observations, specified in the rep(c('case', 'control'), c(2,3)) functions, and the time column, that contains a random number generation with normal distribution (using rnorm() function))

    df ## Rmarkdown allow us to visualize with better conditions the data.frame as a table. If you want to visualize better the data.frame, you can also do that by: View(df) or clicking at the right-top menu on the name of the data.frame

    ##      type       time
    ## 1    case  0.5866135
    ## 2    case  1.2137818
    ## 3 control  1.5495492
    ## 4 control -0.8609144
    ## 5 control -0.7227695

You can also subset the data.frame easily on the same way of a matrix.
However, the data frame structure also allows us to subset by row
position or column position, but also by column and row name. In that
filter, you can filter values of a column by logical operators. For
example:

    df[1, 2] ##subsetting by column and row positions

    ## [1] 0.5866135

    df[,"type"] ## subsetting by column name

    ## [1] "case"    "case"    "control" "control" "control"

    df$type ## In a data.frame, you can select the column by $

    ## [1] "case"    "case"    "control" "control" "control"

    df[df$time < 0.6 & df$time > 0.1,] ## Here, we subset the data.frame by a range contained in a numeric column (time). In this sentence, we subset the data.frame by the contained values of an interval between 0.1 and 0.6

    ##   type      time
    ## 1 case 0.5866135

    df[!df$type=='case',] ## here, we subset by an specific string 'we want to filter only the observations in type column which are not 'case'.

    ##      type       time
    ## 3 control  1.5495492
    ## 4 control -0.8609144
    ## 5 control -0.7227695

To manipulate data easily, R also has a package oriented to this
purpose. His name is dplyr and you can also filter by rows, select
columns or find the coincidences among two columns or data.frames. More
information at:
<a href="https://dplyr.tidyverse.org/" class="uri">https://dplyr.tidyverse.org/</a>

Lists

List are another powerful tool in R because of the content of ordered
set of elements. In addition, you can also subset lists. For example:

    lst <- list(a=1:3, b='hello', fn=sqrt) ## index 3 contains the function "square root"

    lst

    ## $a
    ## [1] 1 2 3
    ## 
    ## $b
    ## [1] "hello"
    ## 
    ## $fn
    ## function (x)  .Primitive("sqrt")

    lst$fn(49) ## Output the square root of 

    ## [1] 7

    lst[1] ## returns a list with the data contained in position 1 (preserves the type of data as a list)

    ## $a
    ## [1] 1 2 3

    lst[[1]] ## returns the data contained in positon 1

    ## [1] 1 2 3

Data structure conversion

Data structures can be interconverted from one type to another.
Depending on the package, some specific structure could be required, and
it is very useful to change it. For example:

    as.matrix (df) ## Convert dataframe into a matrix

    ##      type      time        
    ## [1,] "case"    " 0.5866135"
    ## [2,] "case"    " 1.2137818"
    ## [3,] "control" " 1.5495492"
    ## [4,] "control" "-0.8609144"
    ## [5,] "control" "-0.7227695"

    as.numeric(df$time)      ## Convert text characters into numbers

    ## [1]  0.5866135  1.2137818  1.5495492 -0.8609144 -0.7227695

    as.data.frame(df) ## Convert a matrix into a data frame

    ##      type       time
    ## 1    case  0.5866135
    ## 2    case  1.2137818
    ## 3 control  1.5495492
    ## 4 control -0.8609144
    ## 5 control -0.7227695

    as.character(df$type) ## convert numbers into text chars

    ## [1] "case"    "case"    "control" "control" "control"
