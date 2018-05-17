import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# import flux
df = pd.read_csv('data.csv')
wlength = list(df['Wavelength'])
flux = list(df['Flux'])

# import cross section
df1 = pd.read_csv('hcs2.csv')
clength = list(df1['w'])
csc = list(df1['cs'])


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
        grad = (csc[r]-csc[l])/(clength[r]-clength[l])
        return csc[l]+grad*(wlength-clength[l])
        # return  (csc[r]+csc[l])/2

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

wlength = list(wlength)
wwidth = width(wlength)
k_rate = []
height = []

for i in range(len(wlength)-1):
    k = flux[i]*cal_csc(wlength[i])
    k_rate.append(k*(10**-18))
    height.append(k*(10**-18)/wwidth[i])


plt.yscale('log')
plt.xlim([0,20000])
plt.ylim([10e-11,10e-3])
plt.plot(wlength[:-43],height[:-42])

print('The total reaction rate is :',sum(k_rate))
plt.show()
