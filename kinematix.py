#!/usr/bin/env python

"""Given recorded GPS coordinates, sets for x and t: will compute the 
velocity v_i and acceleration a_i from these position coordinates. 
Using finite difference approximations, we are given some formulas for 
v_i and a_i. """

#assume dt is always a given, so for any set of x, the dt between each 
# x is given. aka, assume the set given to you is well formatted.


def kinematics(x, i, t):
    """Will calculate velocity and acceleration given well-formatted 
    data set of positions."""

    if i<1 or i>(len(x)-1):
        return 0
    else: 
        v = (x[i+1] - x[i-1])/(t[i+1]-t[i-1]) 
        a = (2/(t[i+1]-t[i-1]))*((x[i+1]-x[i])/(t[i+1]-t[i]) - (x[i]-x[i-1])/(t[i]-t[i+1]))
        return v, a
        

def test_kinematics():
    t = [0, .5, 1.5, 2.2]
    x = []
    k = range(len(t))
    for i in k:
        x.append(6*t[i])
    return kinematics(x, 2, t)
    

print test_kinematics()

