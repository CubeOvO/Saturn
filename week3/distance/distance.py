# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:30:49 2018

@author: samsung
"""
import pandas as pd
import numpy as sp
#%%
#distance of Enceladus
d = 2.38*10**8

#rotation period of Saturn, in sec
T = 10*60*60 + 32*60 + 35

# angular velocity
w = 2*sp.pi/T

# calculate length travelled
def length(t):
    l = w*d*t
    return l

# import krate
dt = pd.read_csv('summary.csv')
chem = list(dt['chemical'])
k_rate = list(dt['k_rate'])

lenglist = []
for i in range(len(k_rate)):
    l = length(1/(k_rate[i]))
    lenglist.append(l)
    
for i in range(len(k_rate)):
    print(str(chem[i])+' will go '+str(lenglist[i])+' meters.')
#%%

# kilometer version
lenglistkm = []

for i in range(len(k_rate)):
    l = length(1/(k_rate[i]))/1000
    lenglistkm.append(l)
    
for i in range(len(k_rate)):
    print(str(chem[i])+' will go '+str(lenglistkm[i])+' kilometers.')