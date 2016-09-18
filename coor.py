#!/bin/bash/env python
import math 

#We want to generate n+1 equally spaced x coordinates in [a,b]. Store the coordinates in a list.
#What we want to get in our standard output is a list of numbers that correspond to where the spacing would be

def equalSpacedCoordinates(n, a, b):	
    """n , a and b are integer parameters. n is the number of spaces you want. a and b make the interval to space. This function will take the input parameters and then output a list with its memebers being the coordinates on the x-axis where the spaces are located."""
    coorList = []
    i = 0
    x = float(a)
    #defining the equal spaces
    h = float(b-a)/n

    for i in range(n): #this loop calculates all the values in the list that it will output
        x += h
        coorList.append(x)
    return(coorList)

def test_equalSpacedCoordinates():
    """Function following nosetest procedure to test the equalSpacedCoordinates function """
    eqSpacedList = [0.0, 0.25, 0.5, 0.75]
    function = equalSpacedCoordinates(4,0,1)
    if function == eqSpacedList:
        assert True
       
#these lines take in user input to be fed into the function
def main():
    """ the main method.  """
    steps = int(raw_input("Please enter the number of steps you'd like: "))
    startInterval = float(raw_input("Please enter the beginning of the interval: "))
    endInterval = float(raw_input("Please enter the end of the interval: "))

    print equalSpacedCoordinates(steps, startInterval, endInterval)

if __name__ == "__main__":
    #from sys import argv
    main()


### INSTRUCTOR COMMENTS
#
# Remember the python style convention that you should have no more than
# 80 characters per line. You can format your function docstrings over
# multiple lines. Format them so that they are easy to read and useful.
# For pointers, you can call "help(function)" on any python function in
# a python interpreter (ipython on the command line). You should try to
# model your own docstrings to match those of existing python functions.
#
# Use xrange instead of range when possible. xrange is a generator so it
# only stores the algorithm for generating the next integer as needed.
# range returns a full list, which takes up space in memory if you don't
# need it.
#
# If you are using list.append(item), consider rephrasing your algorithm
# as a list comprehension if possible. For example:
#   l = [a + i*h for i in xrange(n)]
#
# When creating intervals, decide whether you wish to include the endpoints
# or not. Indicate your choice clearly in the docstring. You want to follow
# the "principle of least surprise" for users who want to use your code.
#
# The function "assert" takes a Boolean test. Thus you should just do
#   assert function == eqSpacedList
#
# 
