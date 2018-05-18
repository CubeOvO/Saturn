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
dk = pd.read_csv('summary.csv')
chem = list(dk['chemical'])
k_rate = list(dk['k_rate'])


# calculate the k_rate for each chemical
real_krate = []
for i in range(len(k_rate)):
	k = distance**-2*k_rate[i]
	real_krate.append(k)
print(real_krate)


#%%
# plot config
plt.xlabel("Distance(AU)")
plt.ylabel("Reaction Rate(s^-1)")
plt.yscale('log')
plt.xlim(0,13)
plt.grid()

# plot krate for each chemical

plt.title('krate for each chemical')
for i in range(len(real_krate)):
	plt.plot(distance, real_krate[i],label=chem[i])
plt.legend()
plt.show()
#%%

# calculate the halflife for each chemical
halflife = []
for i in range(len(real_krate)):
	k = real_krate[i]**-1
	halflife.append(k)

# plot
plt.xlabel("Distance(AU)")
plt.ylabel("Half life(s)")
plt.yscale('log')
plt.ylim(10**-3,10**4)
plt.grid()

# plot half life for each chemical
for i in range(len(halflife)):
	plt.plot(distance, halflife[i],label=chem[i])
plt.legend()
#%%
plt.title(' half life for each chemical')
# plot earth, jupiter, Saturn
plt.plot(sp.linspace(1,1,100),sp.linspace(10**-3,10**4,100),color='grey')
plt.plot(sp.linspace(5.2,5.2,100),sp.linspace(10**-3,10**4,100),color='grey')
plt.plot(sp.linspace(9,9,100),sp.linspace(10**-3,10**4,100),color='grey')
plt.show()
