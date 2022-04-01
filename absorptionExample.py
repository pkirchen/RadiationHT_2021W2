# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:32:20 2020

evaluate lorentz lineshape 

@author: pkirchen
"""
from hapi import *
import numpy as np
import matplotlib.pyplot as plt

# Specify some constants
Ru=8.314    # Universal gas constant [kJ/kmol/K]
Na=6.022e23 # Avagadro's number [molecules/mol]

# Species properties 
T = 298     # Temperature [K] (Hitran default value)
yi = 500e-6 #0.05 # Species mole fraction [-]
pt = 1    # total pressure [atm]
pi = yi * pt    # partial pressure [atm]
pl = 200    # Pathlength [cm] 

# Specify database folder 
db_begin('data')

sp = 'CO2'

# Download line data (name, index, isotope, wavenumber min, wavenumber max)
fetch(sp,2,1,2000, 2100)

# output a summary of the line data that was retrieved 
describeTable(sp)

# Return the line data 
# select(sp)

#  Calculate absorption coefficient [cm2/molecule]... absoption cross section
nuL,coefL = absorptionCoefficient_Voigt(SourceTables=sp,
                                          Environment={'T':T,'p':pt})

# Account for species concentration 
nMolec = (pi*101325)*Na/Ru/T*1e-6
abCoef = coefL*nMolec
absorp = 1 - exp(-abCoef*pl)


lam = 1/nuL*1e7
# lam =nuL

plt.close('all')
fig1 = plt.figure(figsize=[8,9])

ax = fig1.add_subplot(2,1,1,yscale='linear',xscale='linear')
ax.plot(lam,coefL)
plt.ylabel(r'$\kappa_{\lambda}$ (Voigt) [cm$^2$/molecule]')
plt.text(0.05, 0.9,
         ' '+sp+'\n Y='+str(yi)+'\n T='+str(T)+'K \n p='+str(pt)+'atm',
         transform = ax.transAxes,
         horizontalalignment = 'left',
         verticalalignment = 'top')

ax = fig1.add_subplot(2,1,2,yscale='linear',xscale='linear')
ax.plot(lam,absorp)
plt.ylabel(r'$\alpha_{\lambda}$ [-]')
plt.text(0.05, 0.9,
         ' '+sp+'\n Y='+str(yi)+'\n T='+str(T)+'K \n p='+str(pt)+'atm\n '+ 'Pathlength='+str(pl)+'cm',
         transform = ax.transAxes,
         horizontalalignment = 'left',
         verticalalignment = 'top')
# ax.plot(1/nuL*1e7,absorptance)


# nuL,coefL_F = absorptionCoefficient_Lorentz(SourceTables=sp, 
#                                           Environment={'T':T,'p':pt},
#                                           Diluent={'self':yi, 'air':1-yi},
#                                           HITRAN_units=False)
# nu, absorpHAPI = absorptionSpectrum(nuL, coefL_F, Environment={'l':pl})

# ax = fig1.add_subplot(3,1,3,yscale='linear',xscale='linear')
# ax.plot(nuL, absorpHAPI)
# plt.ylabel(r'$\alpha$ (HAPI)')

# # fig2 = plt.figure()

#          # nuG,coefG,
#          # nuV,coefV)
