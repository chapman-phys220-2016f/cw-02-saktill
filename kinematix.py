#!/usr/bin/env python
import math
"""Given recorded GPS coordinates, sets for x and t: will compute the 
velocity v_i and acceleration a_i from these position coordinates. 
Using finite difference approximations, we are given some formulas for 
v_i and a_i. """

#assume dt is always a given, so for any set of x, the dt between each 
# x is given. aka, assume the set given to you is well formatted.


def kinematics(x, i, dt=1E-6):
    """Will calculate velocity and acceleration given well-formatted 
    data set of positions x[] and desired position i."""
    dt = 1E-6
    v = []
    a = []
    for k in range(1, len(x)-2):    
    #for each value of the x, this appends v[] appropriately
        r = (x[k+1] - x[k-1])/(2.0*dt)
        v.append(r)
        a.append((1.0/dt)*((x[k+1]-x[k])/dt - (x[k]-x[k-1])/dt))
    return v[i], a[i]

def test_kinematics():
    """tests kinematics function across three time inputs (0, .5, 1.5, 2.2),
    with x_i=Vt_i, where V is some constant. In this test, V=6. """
    dt=1E-6
    V=6
    x = []
    for i in range(int(2.2/dt)+4):
        # adds position values into x[]; splits a certain time range into
        # t/dt and calculates position x based on the formula
        x.append(V*i*dt)
    return (kinematics(x, 0), kinematics(x, int(.5/dt)), kinematics(x, int(1.5/dt)), kinematics(x, int(2.2/dt)))
    assert True
