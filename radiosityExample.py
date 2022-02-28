# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:20:31 2020

Radiosity example for two surface enclosure

@author: pkirchen
"""

import numpy as np
import radiosity as r

#Define shape factors:
a1 = 0.5
a2 = 0.05*a1

f21 = 1
f22 = 0
f12 = a2/a1*f21
f11 = 1-f12

f = np.array([[f11, f12], [f21, f22]])

T = np.array([500.0, 0])

eps  = np.array([0.7, 1])

qr = r.rad_encl_q(f,T,eps)

for i in range(qr.size):
    print ('Incident flux on surface {:1} = {:.4} W/m2'.format(i+1,qr[i]))  
    
    
# Calculate apparent emissivity 
eps_a = -qr[1]/(5.67e-8*T[0]**4)
print('Apparent emissivity = {:.4} [-]'.format(eps_a))
    
