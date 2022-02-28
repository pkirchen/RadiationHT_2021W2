# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:58:19 2020

example for radiative exchange using non gray surfaces. 


@author: pkirchen
"""
import numpy as np
import planck as p

# vector of emissivities for thre spectral regions of interest
e = np.array([[0.4, 0.8, 0.8], [0.7, 0.7, 0.3]])
sig = 5.67e-8

T1 = 1680.0
T2 = 1120.0

# evaluate black body emissive power fractions 
F = np.array([[p.blackF(3*T1), p.blackF(5*T1)-p.blackF(3*T1), 1-p.blackF(5*T1)], 
      [p.blackF(3*T2), p.blackF(5*T2)-p.blackF(3*T2), 1-p.blackF(5*T2)]])

q=0

# solve master net flux equation for all spectral regions
for j in range(3):
    qj = sig*(F[0,j]*T1**4 - F[1,j]*T2**4)/(1/e[0,j] + (1-e[1,j])/e[1,j])
    q = q+qj
    
print('Net flux through surfaces q={:.4} kW/m^2'.format(q/1e3))    
