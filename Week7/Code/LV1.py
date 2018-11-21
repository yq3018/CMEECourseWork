#!/usr/bin/env python3

"""draw Lotka-Volterra model"""

__appname__ = 'LV1.py'
__author__ = 'Yuxin Qin (yq3018@imperial.ac.uk)'
__version__ = '0.0.1'


import scipy as sc
import scipy.integrate as integrate

def dCR_dt(pops, t=0):
    """ define the model """
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    return sc.array([dRdt, dCdt])

type(dCR_dt)

r = 1.
a = 0.1 
z = 1.5
e = 0.75

t = sc.linspace(0, 15,  1000)

R0 = 10
C0 = 5 
RC0 = sc.array([R0, C0]) 

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)

pops

type(infodict)

infodict.keys()

infodict['message']

import matplotlib.pylab as p

f1 = p.figure()

p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')

f1.savefig('../Result/LV1_model1.pdf') #Save figure

f2 = p.figure()

p.plot(pops[:,0], pops[:,1], 'r-')
p.axis([5,42,2.5,25])
p.grid()
p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Cosumer density')
p.title('Consumer-Resource population dynamics')

f2.savefig('../Result/LV1_model2.pdf') #Save figure