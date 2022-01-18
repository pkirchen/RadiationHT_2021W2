# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:41:37 2020

@author: pkirchen
"""

import numpy as np
import planck as pl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch

## Define wavelenght and temperature spaces

lam = np.logspace(np.log10(200e-9), np.log10(5e-6),100)
temp = np.linspace(1400,3000,9)



# Initialize matrix
e=np.zeros([lam.size,temp.size])
i=0
j=0
    
# Calculate emissive power for all lambda/tempeature combinations
for l in lam:
    for t in temp:
        e[i,j] = pl.planck_elb(l,t)/1e6
        j=j+1
    j=0
    i=i+1

# PLOTTING 
# Initialize figurea and axes
fig = plt.figure(1)
ax = fig.add_subplot(1,1,1,yscale="log", xscale="log")

# Plot data, set limits 
ax.plot(lam*1e6,e,linewidth=3)
ax.set_xlim(lam.min()*1e6, lam.max()*1e6)
ax.set_ylim(1e3, 1.5*e.max())

# Generate patch to show visible spectrum
lmin = 0.4
lmax = 0.74
emin = ax.get_ylim()[0]
emax = ax.get_ylim()[1]
patch = ptch.Rectangle((lmin, emin), lmax-lmin, emax-emin, color='0.5', alpha=0.5)
ax.add_patch(patch)

#label axes
ax.set_ylabel("Spectral Emissive Power, $E_{\lambda,b}$ [W/m$^2$/$\mathrm{\mu m}$]")
ax.set_xlabel("Wavelength, $\lambda$ [$\mathrm{\mu m}$]")

# Generate legend text 
temp_l = temp.tolist()
lgt = ['{:.0f} K'.format(m) for m in temp_l]
ax.legend(lgt)

#ax.grid(which="both")
ax.grid(axis="both", which="major",linewidth=0.5, linestyle='-')
ax.grid(axis="both", which="minor",linewidth=0.5, ls='-',c='0.7')
ax.set_axisbelow("True")
        
# Save figures 
#plt.savefig('Planck_emissivePower.eps')
#plt.savefig('Planck_emissivePower.svg')
#plt.savefig('Planck_emissivePower.png', dpi=300)