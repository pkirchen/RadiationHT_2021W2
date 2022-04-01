# -*- coding: utf-8 -*-
"""


pyroInv calculates the temperature and optical thickness for a specified pair 
of spectral apparent temperatures

@author: pkirchen
"""

import numpy as np
import scipy.optimize as scop
import matplotlib.pyplot as plt
import pyroForward as pyro

h = 6.62607e-34 ## Planck constant [Js]
kb = 1.38065e-23 ## Boltzmann constant [J/K]
c0 = 2.9979e8 ## Speed of light in vacuum [m/s]
n=1 ## index of refraction [-]
c2 = h*c0/kb
c1 = h*c0**2


T_real = 3000
kl_real = 0.78

lam = np.array([0.7e-6, 0.8e-6],dtype=complex)
alpha = np.array(1.39,dtype=complex)

# Ta, i = pyro.Tapp(T_real, kl_real, lam)
Ta = np.array([2864*1.01, 2802],dtype=complex)

def kleq(T,*data):
    '''
    kleq returns the real component of the residual for the KL equality 

    Parameters
    ----------
    T : Float
        Estimated soot temperature 
    *data : sequence of arrays
        lam [nx1] wavelengths [m]
        Ta [nx1] apparent temperatures [K]
        alpha soot emissivity exponent 

    Returns
    -------
    resid.real : float
        residual of KL equality 

    '''
    lam, Ta, alpha = data
    lama = np.power(lam*1e6,alpha)
   
    kleq1 = ( 1 - (np.exp(c2/lam[0]/T)-1)/(np.exp(c2/lam[0]/Ta[0])-1) )
    kleq2 = ( 1 - (np.exp(c2/lam[1]/T)-1)/(np.exp(c2/lam[1]/Ta[1])-1) )
    
    resid = np.power(kleq2,lama[1]) - np.power(kleq1,lama[0])
  
    return resid.real


# Find solution using root finding algorithm (zero crossing)
x0 = Ta.max().real
T = scop.brentq(kleq,
                x0,
                5000,
                args = (lam,Ta,alpha))

#  Calculate kl factors 
kl1 = -(lam[0]*1e6)**alpha*np.log( 1 - (np.exp(c2/lam[0]/T)-1)/(np.exp(c2/lam[0]/Ta[0])-1) )
kl2 = -(lam[1]*1e6)**alpha*np.log( 1 - (np.exp(c2/lam[1]/T)-1)/(np.exp(c2/lam[1]/Ta[1])-1) )


# Output results to screen
print('Actual Temperature: {:.4g} K'.format(T_real))
print('Actual KL: {:.4g}'.format(kl_real))
print('Apparent temperature at {:.4g} nm: {:.4g} K'.format(lam[0].real*1e9, Ta[0].real))
print('Apparent temperature at {:.4g} nm: {:.4g} K'.format(lam[1].real*1e9, Ta[1].real))
print('Calculated Temperature: {:.4g} K'.format(T.real))
print('Calculated KL_12: {:.4g}, KL_21: {:.4g}'.format(kl1.real, kl2.real))




# # %% Find solution using otimization (minimize residual)
# # Ta = np.array([2864, 2802],dtype=np.complex)

## Define new residual function to consider the absoluted difference 
## (to avoid giving large negative residuals as the minimizationsolution)
# def kleq_a(T,*data):
    #     '''
    # kleq_a returns the absolute value of real component of the residual for the KL equality 

    # Parameters
    # ----------
    # T : Float
    #     Estimated soot temperature 
    # *data : sequence of arrays
    #     lam [nx1] wavelengths [m]
    #     Ta [nx1] apparent temperatures [K]
    #     alpha soot emissivity exponent 

    # Returns
    # -------
    # float
    #       absolute value of the residual of KL equality 

    # '''
#     lam, Ta, alpha = data
#     lama = np.power(lam*1e6,alpha)
   
#     kleq1 = ( 1 - (np.exp(c2/lam[0]/T)-1)/(np.exp(c2/lam[0]/Ta[0])-1) )
#     kleq2 = ( 1 - (np.exp(c2/lam[1]/T)-1)/(np.exp(c2/lam[1]/Ta[1])-1) )
    
#     resid = np.power(kleq2,lama[1]) - np.power(kleq1,lama[0])
  
#     return abs(resid.real)


# Nfeval=1
# def callbackF(Xi):
#     global Nfeval
#     print( '{0:4d}   {1: 3.6f}'.format(Nfeval, Xi[0]))
#     Nfeval += 1


## Use scipy minimize to find T with minimum residual     
# T = scop.minimize(kleq_a,
#                   x0,
#                   args=(lam, Ta, alpha),
#                   method = 'Nelder-Mead',
#                   options={'disp':True},
#                   callback = callbackF,
#                   bounds=scop.Bounds(2000,4500))
# print('Calculated Temperature (optimization): {:.4g} K'.format(T.x[0]))


# # # *data = (lam,Ta,alpha)
# tr = np.linspace(1500,3500,100)
# ttest = kleq(tr,*(lam,Ta,alpha))

# fig,ax = plt.subplots()
# ax.plot(tr,ttest)
# ax.set_xlabel('Actual Temperature [K]')
# ax.set_ylabel('KL equality residual')
# ax.grid()
