# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:18:49 2020

Demonstrate random number selection for position on a circle.

@author: pkirchen
"""

import numpy as np
import matplotlib.pyplot as plt

r0=1

# Generate random numbers
n = 10000
r1 = np.random.uniform(0,1,n)
r2 = np.random.uniform(0,1,n)

## Example of what happens when uniform distribution isn't used 
# r1 = np.random.normal(0.5, 0.15,n)
# r2 = np.random.normal(0.5,0.15,n)


# Check if distirubtion is uniform
plt.close('all')
fig1 = plt.figure(1,figsize=[6.4,6.4])
plt.hist(r1, bins=20)
fig1.savefig('distn_'+str(n))

# Map random positions 
phi = 2*np.pi*r2
r = r0 * np.sqrt(r1)
#r = r0*r1
x = r*np.cos(phi)
y = r*np.sin(phi)

fig2 = plt.figure(2,figsize=[6.4,6.4])
ax2 = plt.gca()
ax2.plot(x,y,marker='o', markersize=2, mec = 'k', mfc='k', ls='')
ax2.set_xlim([-1,1])
ax2.set_ylim([-1,1])

fig2.savefig('discEmission_'+str(n))