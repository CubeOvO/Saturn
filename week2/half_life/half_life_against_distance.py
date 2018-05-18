# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:42:53 2018

@author: samsung
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as sp
#%%
distance = sp.linspace(0.1,12,100)
#%%
dk = pd.read_csv('summary.csv')
k_rate = list(dk['k_rate'])
#%%
realk_rate = []
for i in range(len(distance)):
    k = k_rate/(distance[i])**2
    realk_rate.append(k)
#%%
plt.xlabel("Distance(AU)")
plt.ylabel("Reaction Rate(s^-1)")
plt.yscale('log')
plt.xlim(0,13)
plt.grid()
plt.plot(distance, realk_rate)
#%%
halflife = []
for i in range(len(realk_rate)):
    h = 1/(realk_rate[i])
    halflife.append(h)
#%%
plt.xlabel("Distance(AU)")
plt.ylabel("Half life(s)")
plt.yscale('log')
plt.ylim(10**-3,10**4)
plt.grid()
plt.plot(distance, halflife)
plt.plot(sp.linspace(1,1,100),sp.linspace(10**-3,10**4,100),color='grey')
plt.plot(sp.linspace(5.2,5.2,100),sp.linspace(10**-3,10**4,100),color='grey')
plt.plot(sp.linspace(9,9,100),sp.linspace(10**-3,10**4,100),color='grey')

plt.legend(, )
