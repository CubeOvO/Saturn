# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:57:47 2018

@author: samsung
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as sp


# estimate a given cross-section using data provided
def cal_csc(wlength):
    l,r = 0,0

    # find the position of the wavelength
    for i in range(len(clength)):
        if(clength[i]>=wlength):
            l, r = i - 1, i
            break
        pass

    # max interplot wavelength < 16419
    if not (l or r):
        # print('out of reach!')
        return 0
    # interplot wavelength
    else:
        #grad = (csc[r]-csc[l])/(clength[r]-clength[l])
        #return csc[l]+grad*(wlength-clength[l])
        return  (csc[r]+csc[l])/2
# cal width
def width(w):
    '''
    :param w: a list containing increasing numbers
    :return: a list denoting the difference between each number
    '''
    d_w = []
    for i in range(len(w)):
        if i < len(w)-1:
            d_w.append(w[i+1]-w[i])
    return d_w
#%%
# import solar flux
df = pd.read_csv('data.csv')
wlength = list(df['Wavelength'])
flux = list(df['Flux'])
#%%

'''
Calcultate the csc for H2O-
'''
# import cross section for H2O-
df1 = pd.read_csv('H2O-.csv')
clength = list(df1['w'])
csc = list(df1['cs'])
#%%
wlength = list(wlength)
wwidth = width(wlength)
k_rate_h2o = []
height = []
for i in range(len(wlength)-1):
    k = flux[i]*cal_csc(wlength[i])
    k_rate_h2o.append(k*(10**-18))
    height.append(k*(10**-18)/wwidth[i]) #=/bin width

# plot config
plt.yscale('log')
plt.xlim([0,10000])
plt.ylim([10e-14,10e-3])
plt.plot(wlength[:-1],height)
plt.title('Reaction Rate of H2O')
plt.xlabel('WAVELENGTH (A)')
plt.ylabel('LOG RATE COEFFICIENT (s-1 A-1)')
print('The total reaction rate of H2O- is :',sum(k_rate_h2o),'s^-1')
plt.savefig('h2o.jpg')
plt.show()
#%%


'''
Calcultate the csc for OH-
'''

# import cross section for hydroxide
df1 = pd.read_csv('hydroxide.csv')
clength = list(df1['w'])
csc = list(df1['cs'])
#%%
wlength = list(wlength)
wwidth = width(wlength)
k_rate_hydro = []
height = []
for i in range(len(wlength)-1):
    k = flux[i]*cal_csc(wlength[i])
    k_rate_hydro.append(k*(10**-18))
    height.append(k*(10**-18)/wwidth[i]) #=/bin width

# plot config
plt.yscale('log')
plt.title('Reaction Rate of OH-')
plt.plot(wlength[:-1],height)
plt.xlabel('WAVELENGTH (A)')
plt.ylabel('LOG RATE COEFFICIENT (s-1 A-1)')
print('The total reaction rate of OH- is :',sum(k_rate_hydro),'s^-1')
plt.savefig('hydro.jpg')
plt.show()
#%%
distance = sp.linspace(0.1,12,100) # from sun to 12 AU

