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
lam = np.logspace(-7, np.log10(50e-6),100)
temp = np.array([300, 2000, 5000])

# Initialize matrix
#elt=np.zeros([lam.size*temp.size])
i=0
j=0
lt = np.zeros([temp.size, lam.size])
elt = np.zeros([temp.size, lam.size])
#elt = np.array([])
#elt=0.0

fig = plt.figure(1)
ax = fig.add_subplot(1,1,1,yscale='linear',xscale='log')
ln=[]
    
# Calculate emissive power for all lambda/tempeature combinations
for t in temp:
    for l in lam:
#        lt=np.append(lt,l*t)
#        elt=np.append(elt, pl.planck_lt(lt[-1]))
        lt[i,j] = l*t
        elt[i,j] = pl.planck_lt(lt[i,j])
        j = j+1
    j = 0
    i = i+1    
#    ln.append(ax.plot(lt*1e6,elt, linestyle='none',marker='x'))
#    lt = np.array([])
#    elt = np.array([])
#        j=j+1
#    j=0
#    i=i+1

# PLOTTING 
# Initialize figurea and axes

#ln[0][0].set_color('r')
#ln[1][0].set_color('g')

# Plot data, set limits 
lines = ax.plot(np.transpose(lt)*1e6,np.transpose(elt),
                linestyle='none',marker='x', markeredgewidth=2, markersize=8)
#ax.set_xlim(1e2, 1e6)
ax.set_xlim(500, 50000)
ax.set_ylim(0, 1.5e-11)

# Generate patch to show visible spectrum
#lmin = 0.4
#lmax = 0.74
#emin = ax.get_ylim()[0]
#emax = ax.get_ylim()[1]
#patch = ptch.Rectangle((lmin, emin), lmax-lmin, emax-emin, color='0.5', alpha=0.5)
#ax.add_patch(patch)

#label axes
ax.set_ylabel("Spectral Emissive Power/T$^5$, $E_{\lambda,b}$ [W/m$^2$/$\mathrm{\mu m}/$T$^5$]")
ax.set_xlabel("Wavelength*Temperature, $\lambda T$ [$\mathrm{\mu mK}$]")

# Generate legend text 
temp_l = temp.tolist()
lgt = [str(m)+' K' for m in temp_l]
ax.legend(lgt)

#ax.grid(which="both")
ax.grid(axis="both", which="major",linewidth=0.5, linestyle='-')
ax.grid(axis="both", which="minor",linewidth=0.5, ls='-',c='0.7')
ax.set_axisbelow("True")
#ax.plot(t,(y[:,2]),label='Pressure',linewidth=3,linestyle='--')
        
# Save figures 
plt.savefig('Planck_emissivePower_lamT.eps')
plt.savefig('Planck_emissivePower_lamT.svg')
plt.savefig('Planck_emissivePower_lamT.png', dpi=300)