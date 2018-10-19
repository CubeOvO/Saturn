# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:13:23 2018

@author: samsung
"""
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from h_theory import *



def main():
    df = pd.read_csv('hydroxide.csv') # read data
    wlength = list(df['w'])
    crosss = list(df['cs'])

    en = length_ev(wlength) # convert to energy

    plotsigma(3.3*10**-17, 1.8, en) # plot graph for theory

    cross = [x*10**-18 for x in crosss]
    w = width(wlength)
    plt.plot(en[:-1], cross[:-1],'.') # plot graph for data
    plt.show()

    var(3.3*10**-17, 1.8,en) # variance
     
    
    
    
if __name__ == "__main__":
    main()
