# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:32:20 2020



@author: pkirchen
"""
from hapi import *
import numpy as np
import matplotlib.pyplot as plt

# Specify some constants
Ru=8.314    # Universal gas constant [kJ/kmol/K]
Na=6.022e23 # Avagadro's number [molecules/mol]

# Species properties 
T = 1000.0     # Temperature [K] (Hitran default value)
yi = 1.0 # Species mole fraction [-]
pt = 0.1    # total pressure [atm]
pi = yi * pt    # partial pressure [atm]
pl = 100    # Pathlength [cm] 

# Specify database folder 
db_begin('data')

sp = 'CO2'

# Download line data 
fetch(sp,2,1,2000.0,2100.0)

# output a summary of the line data that was retrieved 
describeTable(sp)

# Return the line data 
# select(sp)

#  Calculate absorption coefficient [cm2/molecule]
nuL,coefL = absorptionCoefficient_Lorentz(SourceTables=sp,
                                          Environment={'T':T,'p':pt})

# nuG,coefG = absorptionCoefficient_Doppler(SourceTables=sp,
#                                           WavenumberStep=0.0001,
#                                           Environment={'T':T,'p':pt})

nuV,coefV = absorptionCoefficient_Voigt(SourceTables=sp,
                                        Environment={'T':T,'p':pt})

plt.close('all')
fig1 = plt.figure(figsize=[8,9])

ax = fig1.add_subplot(2,1,1,yscale='linear',xscale='linear')
ax.plot(nuL,coefL)
plt.ylabel(r'$\kappa_{\lambda}$ (Lorentzian) [cm$^2$/molecule]')
plt.text(0.05, 0.9,
         ' '+sp+'\n Y='+str(yi)+'\n T='+str(T)+'K \n p='+str(pt)+'atm',
         transform = ax.transAxes,
         horizontalalignment = 'left',
         verticalalignment = 'top')


# ax = fig1.add_subplot(3,1,2,yscale='linear',xscale='linear')
# ax.plot(nuG,coefG)
# plt.ylabel(r'$\kappa_{\lambda}$ (Gauss) [cm$^2$/molecule]')

ax = fig1.add_subplot(2,1,2,yscale='linear',xscale='linear')
ax.plot(nuV,coefV)
plt.ylabel(r'$\kappa_{\lambda}$ (Voigt) [cm$^2$/molecule]')
plt.xlabel(r'$\eta$ [cm$^{-1}$]')

