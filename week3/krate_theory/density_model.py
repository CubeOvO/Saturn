# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:52:33 2018

@author: samsung
"""
import matplotlib.pyplot as plt
import numpy as sp

# range of distance
R = sp.linspace(5,11,100)

# equation : n = A exp (-B (R/RS)2)a
def cal_d(A, B, R):
    return A*sp.exp(-B*R**2)

# radius of Saturn, in meter, Rs = 58232000

# plotting graph, constants for nW+nH (from Wilson 2008)
a = 167.3
b = 0.041
density = []
for i in range(len(R)):
	p = cal_d(a,b,R[i])
	density.append(p)

plt.xlabel("Distance(Rs)")
plt.ylabel("Ion Density(cm^-3)")
plt.plot(R, density)
plt.yscale('log')
plt.ylim(1,100)
plt.grid()
plt.savefig('d')
plt.show()