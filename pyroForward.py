# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:43:39 2020

pyroForward calculates the apparent temperature and intensity for a given temperature and KL

Inputs
    T (float): temperature [K]
    kl (float): kl factor [-]
    lam (float): wavelength [m]
    
Returns
    Tapp (float): Apparent temperature [K]
    i (float): Intensity [W/m2/sr/um]

@author: pkirchen
"""

import planck as plk
import numpy as np


# T = 3000
# kl = 0.78
# lam = np.array([0.7e-6, 0.8e-6]) #[m]
alpha = 1.39

def Tapp(T,kl,lam):
    i = plk.planck_elb(lam,T)*1e-6/np.pi * (1-np.exp(-kl/((lam*1e6)**alpha))) # [W/m2/um/sr]
    Tapp = plk.appT(i*1e6,lam) #[K]
    
    return Tapp, i

# print(i)
# print(Tapp)

