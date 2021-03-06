#!/usr/bin/env Rscript
# Author: Yuxin Qin yq3018@imperial.ac.uk
# Script: basic_io.R
# Description: read and write csv in R
# Date: Oct 2018

# A simple script to illustrate R input-output.  
# Run line by line and check inputs outputs to understand what is happening  

MyData <- read.csv("../Data/trees.csv", header = TRUE) # import with headers

write.csv(MyData, "../Result/MyData.csv") #write it out as a new file

write.table(MyData[1,], file = "../Result/MyData.csv",append=TRUE) # Append to it

write.csv(MyData, "../Result/MyData.csv", row.names=TRUE) # write row names

write.table(MyData, "../Result/MyData.csv", col.names=FALSE) # ignore column names
