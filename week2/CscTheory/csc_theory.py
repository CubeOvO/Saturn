# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:13:23 2018

@author: samsung
"""
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

#%%
# First attempt, plotting the empirical formula for H-

#%%
# convert wavelength, wlength, to energy in eV, en

def length_ev(w):
    ev = []
    for i in range(len(w)):
        k = ((6.63*10**-34)*3*10**8)/((w[i]*10**-10)*1.6*10**-19)
        ev.append(k)
    return ev

#%%
# a range of values for energy
# calculate sigma (y-axis)
def plotsigma(sigin, ea, energy):
    a = min(energy)-1
    if a<0:
        a = 0
    e = sp.linspace(a,max(energy)+1,100)
    
    sigma = []
    for i in range(len(e)):
        y = sigin*(1-ea/e[i])**0.5
        sigma.append(y)
    plt.plot(e,sigma)
    
    plt.grid(True)

   

def var(sigin, ea, data): # calculate variance
    v = []
    for i in range(len(data)):
        k = data[i]-sigin*(1-ea/data[i])**0.5
        v.append(k**2)
    print(sum(v)/len(data))
        
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

def main():
    df = pd.read_csv('hcs_latest.csv') # read data
    wlength = list(df['w'])
    crosss = list(df['cs'])

    en = length_ev(wlength) # convert to energy
    
    plotsigma(10**-17, 0.75, en) # plot graph for theory

    cross = [x*10**-18 for x in crosss]
    w = width(wlength)
    print(w)
    crossd = [x/y for x,y in zip(crosss[:-1],w)]
    plt.plot(en[:-1], cross[:-1],'.') # plot graph for data
    plt.show()

    var(10**-17, 0.75,en) # variance
     
    
    
    
if __name__ == "__main__":
    main()
