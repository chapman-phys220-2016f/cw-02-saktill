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
    print(coorList)

#these lines take in user input to be fed into the function 
steps = int(raw_input("Please enter the number of steps you'd like: "))
startInterval = float(raw_input("Please enter the beginning of the interval: "))
endInterval = float(raw_input("Please enter the end of the interval: "))

equalSpacedCoordinates(steps, startInterval, endInterval)


