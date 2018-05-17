import pandas as pd
import numpy as sp
import matplotlib.pyplot as plt

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


df = pd.read_csv('data.csv')

# process flux density
flux = list(df['Flux'].astype(sp.float))
wlength = df['Wavelength']
wwidth = width(wlength)
wdense = []
for i in range(len(wwidth)):
    wdense.append(flux[i]/wwidth[i])

# plot
plt.xlabel('LOG WAVELENGTH (A)')
plt.ylabel('LOG PHOTONS (cm-2 s-1 A-1)')
plt.loglog(wlength[:-1],wdense)
plt.savefig('1.png')
plt.show()