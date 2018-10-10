#!/bin/bash
# Author: Yuxin Qin yq3018@imperial.ac.uk
# Script: variables.sh
# Desc: show the use of variables and read multiple values
# Arguments: bash variables.sh
# Date: Oct 2018

# Shows the use of variables
MyVar='some string'
echo 'the current value of the variable is' $MyVar
echo 'Please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar

## Reads multiple values
echo 'Enter two numbers separated by space(s)'
read a b
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum
