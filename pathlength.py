#!/usr/bin/env python

import math

"""Some object is moving along a path in the plane. At n+1 points of time we 
have recorded the corresponding (x,y) positions of the object: 
(x_0,y_0)...(x_n,y_n). The total length L of the path is the sum of all 
the individual line segments. 
L = sum rad((x_i - x_i-1)^2 + (y_i - y_i-1)^2"""


def pathlength(x, y):
    """This function will calculate the pathlength based on the above formula, 
    given x=[x_1...x_i] and y=[y_1...y_i]"""

    indices = range(len(x))
    
    if len(x) != len(y):
        return 0
    
    else:
        pl = 0
        for i in indices:
            L = math.sqrt((x[i])**2 + (y[i])**2)
            pl += L
        return pl

def test_pathlength():
    """Function for testing the pathlength formula"""
    x=[1,3]
    y=[2,4]
    if(pathlength(x,y) == 2*math.sqrt(2)):
        assert True 

def main():
    """function for implementing pathlength"""
    #found this next list comeprehension on Stack Overflow. Takes user input and appends it to a list.
    print("Please input the same number of x coordinates as y coordinates")
    x = [int(n) for n in raw_input("Enter numbers for x coordinates. Leave spaces inbetween each entry: ").split()]
    y = [int(n) for n in raw_input("Enter numbers for y coordinates. Leave spaces inbetween each entry: ").split()]
    path = pathlength(x,y)
    print "The pathlength for this n-dimensional vector is: ", path

if __name__ == "__main__":
    main()


### INSTRUCTOR COMMENTS
# 
# See previous problem for using docstrings correctly. In particular, saying "as above" makes no sense
# except in source code. You want the docstrings to be sensible when using the help() command within
# an interpreter.
#
# In pathlength you compute something before doing an input sanity check. Always check inputs first.
# 
# Rather than using indices, try to find ways to iterate over elements directly. For example,
#   for xi, yi in zip(x,y):
#     p1 += math.sqrt(xi**2 + yi**2)
# This uses the zip() function to create a list of tuples of matches elements of x and y, then
# unpacks the tuples into xi and yi in the for loop. This is cleaner to read and understand,
# and is less prone to indexing errors.
#
# Again, assert takes a Boolean test directly.
#
# When citing things from StackOverflow, always cite the exact link. Treat it as a citation in a
# paper - improper or missing citations are plagiarism.
# If you are using hints from the web like this, make sure you can code the line yourself and
# understand what every part of it does. Just copy-pasting it is not sufficient without understanding.
