# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:25:40 2020

Monte Carlo consideration of two parallel disks with concentric axes
Calculate the configuration factor 

@author: pkirchen
"""

from mpl_toolkits.mplot3d import Axes3D  # needed for 3d plotting 

import numpy as np 
import matplotlib.pyplot as plt



#%%  Define function to generate, emit, track ray for coaxial, parallel discs
def discF12(n):
    # Define surfaces 
    # Disk 1:
    r1= 1 #m
    a1 = np.pi*r1**2 #m2
    
    # Disk 2
    r2 = 0.5 #m
    a2 = np.pi*r2**2 #m2
    
    # Separation distance
    l = 1 #m
    
    # Analytical view factor 
    fr1 = r1/l
    fr2 = r2/l
    fx = 1 + (1+fr2**2)/fr1**2
    f12a = 0.5*(fx - np.sqrt(fx**2 - 4*(fr2/fr1)**2))
    f21a = a1/a2*f12a
    
    # Generate random numbers
    # n = 100
    r = np.random.random([n,5])
    # random number index:
    #0: azimuthal position, phi_p
    #1: radial position, rad_p
    #2: zenith direction, theta_d 
    #3: azimutal direction, phi_d
    #4: not used
    
    
    
    # Map random positions 
    phi_p = 2*np.pi*r[:,0] # rad
    rad_p = r1 * np.sqrt(r[:,1])  # m
    
    x = rad_p*np.cos(phi_p)  # m 
    y = rad_p*np.sin(phi_p)  # m
    
    # Define emission direction 
    theta_d = np.arcsin(np.sqrt(r[:,2])) # rad
    phi_d = np.pi*2*r[:,3] # rad
    
    # Generate vector
    ux = np.sin(theta_d)*np.cos(phi_d)
    uy = np.sin(theta_d)*np.sin(phi_d)
    uz = np.cos(theta_d)
    
    # Extend rays to l and check for intersection, if rays intersect, then increment counter
    ic = 0 #intersection counter
    for j in range(n) :
        s = l/uz[j]  # m
        xl = x[j]+s*ux[j]  # m
        yl = y[j]+s*uy[j]  # m
        
        if np.sqrt(xl**2+yl**2)<=r2:
            ic = ic+1
    
    # Calculate view factor      
    f12 = ic/n
    f21 = a1/a2*f12
    
    df12 = (f12a-f12)/f12a*100
    df21 = (f21a-f21)/f21a*100
    print('N = {:3}'.format(n))
    print('{:^6}{:^18}{:^18}{:^18}'.format('','Monte Carlo','Analytical','% Diff'))
    print('{:^6}{:^18.4}{:^18.4}{:^18.4}'.format('F12',f12,f12a,df12))
    print('{:^6}{:^18.4}{:^18.4}{:^18.4}'.format('F21',f21,f21a,df21))
    
    
    return f12, df12
    

#%% Example to run calculation to determine view factor 
# Define number of rays
n =100

f12, df12 = discF12(n)


#%% Example with plottin and j repetitions to identify variability 

n =100

df = np.array([])
f = np.array([])

for j in range(20):
    fj,dfj=discF12(n)
    f = np.append(f, fj)
    df = np.append(df, dfj)

fig1 = plt.figure()
ax1 = plt.subplot()
ax1.plot(f)
ax1.set_xlabel('Iteration')
ax1.set_ylabel('View Factor F12')
    
fig2 = plt.figure()
ax2 = plt.subplot()
ax2.plot(abs(df))
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Error (%)')

print('Average error = {:.4}%'.format(np.mean(abs(df))))


    