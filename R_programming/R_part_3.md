General data supervision and graphic plots
------------------------------------------

As a practical case, we will apply the acquired knowledge to a practical
case in R.

For that purpose, we will use the pre-built data frame iris (from
biological data) in order to start a data analysis and data
visualization in R.

First, we build the data into a variable and we visualize the data frame
properly.

    myData <- iris
    head(myData)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    summary(myData)

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

We can visualize the summary of the data displayed above. We can see
that the data are distributed in 5 columns. 4 of the columns are numeric
(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width) and one of the
column is a factor (Species).

If we want to visualize in a graphic mode, the most easy way is by the
use of plot()

    plot(myData)

![](media/R/unnamed-chunk-2-1.png)

If you want to see the points by category (who belongs to setosa,
versicolor or virginica), we can use:

    plot(myData, col=myData$Species) ## col indicates the factor

![](media/R/unnamed-chunk-3-1.png)
If we want to plot variables two-by-two:

    plot(myData$Sepal.Length, myData$Sepal.Width, col=myData$Species)

![](media/R/unnamed-chunk-4-1.png)

We can add to the graphic the plot characters and cex (plot size).

    plot(myData$Sepal.Length, myData$Sepal.Width, col=myData$Species, pch=16, cex=1)

![](media/R/unnamed-chunk-5-1.png)
If we change parameters and we add the legend too:

    plot(myData$Sepal.Length, 
         myData$Sepal.Width, 
         col=myData$Species,
         pch=16) 
    legend(x = 6.1, y = 4.3, 
           legend = levels(myData$Species), 
           col = c(1:3)) ### x and y are the coordinates into the plot

![](media/R/unnamed-chunk-6-1.png)

    ######RUN ONLY IN TERMINAL, not available in Rmarkdown

Changing the parameters, you can change the graphic as you want:

    plot(myData$Sepal.Length,
         myData$Sepal.Width,
         col=myData$Species,
         pch=16,
         main='Iris sepal analysis')
    legend(x = 4, 
           y = 5.5, 
           legend = levels(myData$Species), 
           col = c(1:3), 
           pch = 16)#, box.col = "white" )

![](media/R/unnamed-chunk-7-1.png)
We can see that R is very useful in data visualization. Furthermore, we
are able to make in R different type of graphics depending on our
purposes. For example, if we want how is the distribution of the data,
we can make an histogram easily by hist() function:

    hist(myData$Sepal.Length)

![](media/R/unnamed-chunk-8-1.png)

In addition, we can specify the number of intervals to represent more
accurately the data distribution by the flag breaks=

    hist(myData$Sepal.Length, breaks=20)

![](media/R/unnamed-chunk-9-1.png)

    hist(myData$Sepal.Length, breaks=15, col="red") ## Colour settings

![](media/R/unnamed-chunk-9-2.png)

You can also plot boxplot on your data for a better visualization of
them:

    boxplot(myData$Sepal.Length ~ myData$Species, col=c("red", "green", "purple"))

![](media/R/unnamed-chunk-10-1.png)

If you want to make a barplot:

    list_factors <- c('setosa', 'versicolor', 'virginica')

    for (avg in list_factors){
      
      eval(parse(text=paste0(avg, " <- myData[myData$Species == '", avg, "',]")))
      eval(parse(text=paste0(avg, "_sum <- data.frame(summary(", avg, "))")))
      
    }

ggplot2

In R, we can use the prefixed functions to represent data in graphics,
but also it exists a powerful package to plot graphics with different
designs, becoming more attractive to the public. This package is called
ggplot2 (to explore how ggplots works, please see
<a href="https://ggplot2.tidyverse.org/" class="uri">https://ggplot2.tidyverse.org/</a>)

In ggplot2, compared with base plot functions, we have three fundamental
parts: data, aesthetics and geometry, calling the last two parts
“layers” because they are geometric elements and statistical
transformations. It allow us to create graphics to work in them
interactively, starting with the data to be represented and following
the additiion of layers.

First, you need to install the library ggplot2

    install.packages('ggplot2', repos="http://cran.us.r-project.org")

    ## Installing package into 'C:/Users/David/Documents/R/win-library/4.0'
    ## (as 'lib' is unspecified)

    ## 
    ##   There is a binary version available but the source version is later:
    ##         binary source needs_compilation
    ## ggplot2  3.3.5  3.3.6             FALSE

    ## installing the source package 'ggplot2'

    ## Warning in install.packages("ggplot2", repos = "http://cran.us.r-project.org"):
    ## installation of package 'ggplot2' had non-zero exit status

    library(ggplot2)

    ## Warning: package 'ggplot2' was built under R version 4.0.5

A common order in ggplot to create a scatterplot is:

    ggplot(data=myData, mapping= aes(x=Sepal.Length, y=Sepal.Width, by=Species, color=Species))+
      geom_point()+
      stat_ellipse(geom='polygon',
                   aes(fill=Species),
                   alpha=0.2)

![](media/R/unnamed-chunk-13-1.png)

    ###Here, we can define the three parts of a ggplot: data, aesthetics and geometry. We add stat ellipse too

We can use the same dataset, but plotting other type of data, like:

    ggplot(data=myData, mapping= aes(x=Sepal.Length, y=Sepal.Width, by=Species, color=Species))+
      geom_point()+
      geom_line()

![](media/R/unnamed-chunk-14-1.png)

    ###We have to see that each layer appears on the last one. In that case, we can see the same graphic without ellipse

A common graphics are:

    geom_boxplot() ##To plot boxplots

    ## geom_boxplot: outlier.colour = NULL, outlier.fill = NULL, outlier.shape = 19, outlier.size = 1.5, outlier.stroke = 0.5, outlier.alpha = NULL, notch = FALSE, notchwidth = 0.5, varwidth = FALSE, na.rm = FALSE, orientation = NA
    ## stat_boxplot: na.rm = FALSE, orientation = NA
    ## position_dodge2

    geom_line()  ## To plot tendencies lines

    ## geom_line: na.rm = FALSE, orientation = NA
    ## stat_identity: na.rm = FALSE
    ## position_identity

    geom_point() ## To plot scatterplots

    ## geom_point: na.rm = FALSE
    ## stat_identity: na.rm = FALSE
    ## position_identity

    ggplot(data=myData, mapping= aes(x=Species, y=Sepal.Width, color=Species))+
      geom_boxplot()+
      geom_line()

![](media/R/unnamed-chunk-15-1.png)

We can also plot other kind of graphics to create more attractive data
visualization.

    ggplot(data=myData, aes(x=Sepal.Width, fill=Species, color=Species))+ ##We can play with the transparencies using alpha and the desired vaule
      geom_density(alpha=0.5)

![](media/R/unnamed-chunk-16-1.png)

You can modify the grid too, and turn it off. in addition, we can play
with the titles too by the option labs.

    ggplot(data=myData, aes(x=Sepal.Width, fill=Species, color=Species))+ 
      geom_density(alpha=0.5)+
      theme(panel.grid=element_blank(), panel.background = element_rect(fill='white'), plot.title.position='plot')+ ##Here, we eliminate the grid and change the back colour to white
      labs(title='Density of Sepal Width', subtitle = 'Iris dataset')

![](media/R/unnamed-chunk-17-1.png)
Other examples:

    ggplot(data=myData, mapping= aes(x=Species, y=Sepal.Width, color=Species, fill=Species))+
      geom_violin(trim=FALSE,
                  alpha=0.3)+
      geom_boxplot(width=0.05)+
      theme(panel.grid=element_line(color='black', size=0.5, linetype=3),
            panel.background = element_rect(fill='white'), 
            plot.title.position='plot')+
      labs(title='Violin chart', subtitle = 'Iris dataset')##Violin graphics to representate the density

![](media/R/unnamed-chunk-18-1.png)

    #remotes::install_github("R-CoderDotCom/ggcats@main")
    ggplot(data=myData, mapping= aes(x=Sepal.Width))+
      geom_histogram(aes(y=..density..),
                     colour=1,
                     fill='blue')+
      geom_density(fill='blue', 
                   alpha=0.2)+
      theme(panel.grid=element_line(color='black', size=0.5, linetype=3),
            panel.background = element_rect(fill='white'), 
            plot.title.position='plot')+
      labs(title='Histogram and density chart', subtitle = 'Iris dataset')

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](media/R/unnamed-chunk-19-1.png)

Useful websites and more types of charts:

<a href="https://r-graph-gallery.com/ggplot2-package.html" class="uri">https://r-graph-gallery.com/ggplot2-package.html</a>
<a href="https://ggplot2.tidyverse.org/" class="uri">https://ggplot2.tidyverse.org/</a>
<a href="https://datacarpentry.org/R-ecology-lesson/04-visualization-ggplot2.html" class="uri">https://datacarpentry.org/R-ecology-lesson/04-visualization-ggplot2.html</a>
