#!/usr/bin/env python

"""Given recorded GPS coordinates, sets for x and t: will compute the 
velocity v_i and acceleration a_i from these position coordinates. 
Using finite difference approximations, we are given some formulas for 
v_i and a_i. """

#assume dt is always a given, so for any set of x, the dt between each 
# x is given. aka, assume the set given to you is well formatted.

x = []


def kinematics(x, i, dt=1E-6):
    """Will calculate velocity and acceleration given well-formatted 
    data set of positions and desired position."""
    

    v = []
    a = []

    for k in range(1, len(x)-2):
        r = (x[k+1] - x[k-1])/(2.0*dt)
        v.append(r)
    print(v)
        #a.append((1.0/(dt))*((x[k+1]-x[k])/(dt) - (x[k]-x[k-1])/(dt)))
    #return v[i]

def test_kinematics():
    """tests kinematics function across three time inputs (0, .5, 1.5, 2.2),
    with x_i=Vt_i, where V is some constant. In this test, V=6. """
    dt=1E-6
    V=6

    for i in range(int(.06/dt)+7):
        x.append(V*i)

    print(x)
    #return kinematics(x, int(.5/dt)), kinematics(x, int(1.5/dt))
    

print test_kinematics()

