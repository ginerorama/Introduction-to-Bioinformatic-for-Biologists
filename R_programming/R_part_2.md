Loops and conditionals
----------------------

In R, we can also use loops and conditionals to improve the scripting.
In that case, we can call it cycles too. Loops are usually used to
repeat the same sentences on a sucession. For example, if we have 18
folders and we want to repeat the same order for each one, we can use a
loop to reduce the scripting, like that:

We have 8 folders called folder1…folder8, located in a specific dir.
Each folder has 1 file whose name is the same: data.csv. We want to
calculate the average of the first column of the data. It would be like
that:

    ## Without loop

    #data1 <- read.table(folder1,sep=';')
    #data2 <- read.table(folder2,sep=';')
    #data3 <- read.table(folder3,sep=';')
    #data4 <- read.table(folder4,sep=';')
    #data5 <- read.table(folder5,sep=';')
    #data6 <- read.table(folder6,sep=';')
    #data7 <- read.table(folder7,sep=';')
    #data8 <- read.table(folder8,sep=';')
    #
    ## Calculate the mean
    #
    #mean(data1[,1])
    #mean(data1[,2])
    #mean(data1[,3])
    #mean(data1[,4])
    #mean(data1[,5])
    #mean(data1[,6])
    #mean(data1[,7])
    #mean(data1[,8])
    #
    ### With loop
    #
    #list_dir <- dir(foldersDir) ## List dir from the base folder
    #
    #for (x in list_dir){
    #  
    #  data <- read.table(x, sep=';') #read data
    #  mean(data) #average calculation
    #  
    #}
    #

As we can see here, with a loop, we reduce drastically the scripting and
we optimize the time running the script. It is a powerful tool when we
have a lot of data to be analyzed. In that case, we can divide the loops
in: while() and for(). In R, the loops are composed in two parts
following this structure:

    #for(x in y){##Here, this is a loop that pass on all the given parts of the vector. For example, if the vector is y and #it is composed by 1...9, you will have 9 repetitions, and x would represent the number of repetition where you are #working on (for example, if you are in the third repetition, x=3 (repetition 3 of 9)). It means that: for all these #parts described in this list, please run the following sentences.
    #  
    #  sentences
    #  
    #}
    #
    #
    #while(x<0.05){##Here, we stablish a rule: while x<0.05, please run the following orders or sentences
    #  
    #  sentences
    #  
    #}
    #

Conditionals if() and ifelse()

R also allows us to introduce conditional statements. It is commonly
used as a condition like that:

    x <- 2

    if(x == 1){#### If the comparison x == 1 is TRUE (if x is equal to 1)
      
      print('x is equal to 1')
      
    }else{
      
      print('x is not equal to 1')
      
    }

    ## [1] "x is not equal to 1"

You can use the same structure using the function ifelse():

    ifelse(x==1,'x is equal to 1', 'x is not equal to 1')

    ## [1] "x is not equal to 1"

When you write a condition, it is a logical value TRUE-FALSE the
principal object to decide if execute one sentence. It means that if a
comparison is true, then run this sentence. If not, run the other one.
Furthermore, you can use more than one condition to be satisfied using
else if().

    x <- 2

    if(x == 1){#### If the comparison x == 1 is TRUE (if x is equal to 1)
      
      print('x is equal to 1')
      
    }else if (x < 1){ ## Check if is lower than 1
      
      print('x is lower than 1')
      
    }else{
      
      print('x is higher than 1') ## Check if is higher than 1
      
    }

    ## [1] "x is higher than 1"

Functions
---------

One of the most important part of R is the building of functions. As a
general structure of a function, we could define the functions as:
function(x) (we have used different functions along the tutorial, like
mean(x) to calculate the average of a group of numbers). To build a
function, the common structure is:

    #
    #x <- "Variable for processing"
    #
    #myFunction <- function(x){ ## Here, we are building the function. In this function (myFunction), introducing the #argument (x), the function will realize a print(x)
    #  
    #  print(x)
    #  
    #}
    #
    #myFunction(x)

The functions are designed to realize a serial of operations on a
variable. In a function, you can define the function as a process on a
variable with a return or not. An example is:

    ########################### Without return

    x <- 1

    myFunction <- function(x){ ## Here, we are building the function. In this function (myFunction), introducing the argument (x), the function will realize a print(x)
      
      print(x)
      x <- x + 1
      print(x)
    }

    myFunction(x)

    ## [1] 1
    ## [1] 2

    ############################ With return

    myFunction <- function(x){ ## Here, we are building the function. In this function (myFunction), introducing the argument (x), the function will realize a print(x)
      
      print(x)
      x <- x + 1
      
      return(x)
      
    }

    myResult <- myFunction(x)

    ## [1] 1

    print(myResult)

    ## [1] 2

Load data and pre-built datasets
--------------------------------

To learn R with data, R help us by the use of pre-built data sets only
for practice analysis. Datasets like iris or esoph are very useful when
you learn programming.

    dataset <- iris ## As they are pre-built, you just type the name of the dataset and it will be built in the variable dataset

    head(dataset)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    summary(dataset) ## It realizes a basic statistics of the whole dataset

    ##   Sepal.Length    Sepal.Width     Petal.Length    Petal.Width   
    ##  Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
    ##  1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
    ##  Median :5.800   Median :3.000   Median :4.350   Median :1.300  
    ##  Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
    ##  3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
    ##  Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  
    ##        Species  
    ##  setosa    :50  
    ##  versicolor:50  
    ##  virginica :50  
    ##                 
    ##                 
    ## 

However, in the real life, you have to import your data. Depending on
the format, you will use different kind of functions. For example, when
your data are in .csv data, you will use as separator ‘;’, but when your
data are in .txt data, you will use as separator ’. For example:

    #data <- read.table('pathToMydata.txt', header=TRUE, sep='\t') ## In this expression, we are defining the read table taking account the first raw of the data as header, and the separate data by tabulation

You can also use different functions to read, for example, .xls data
(from Excel) installing the package readxl and using the function
read\_xlsx().

If you want to save your analysis or transformed data whatever the data
format, you can use write.table() and choose the correct format using
the correct separator. Furthermore, you can save your data in .rds
format (as a proper variable of R) using the save function. For example:

    #write.table(myData, file='path/to/my/file.txt', sep='\t') ## Write data in a common way
    #save(myData, file='path/to/my/file.rds') ## Write data in R format 

Save at .rds format it often useful when you are working with higher
structures than data.frames, like S4 objects (used normally in genomic
data from bioconductor packages)
