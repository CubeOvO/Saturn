import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# import flux



def length_ev(w):
    ev = []
    for i in range(len(w)):
        k = ((6.63*10**-34)*3*10**8)/((w[i]*10**-10)*1.6*10**-19)
        ev.append(k)
    return ev

# theory cross section
def sigma(sigin, ea, wavelength):
    energy = length_ev(wavelength)
    sigma = []
    for i in range(len(energy)):
        if energy[i] >= ea:
            y = sigin*(1-ea/energy[i])**0.5
            sigma.append(y)
        else:
            sigma.append(0)
    return sigma


def width(w):
    '''
    :param w: a list containing increasing numbers
    :return: a list denoting the difference between each number
    '''
    d_w = []
    for i in range(len(w)):
        if i < len(w)-1:
            d_w.append(abs(w[i+1]-w[i]))
    return d_w

def main():
    df = pd.read_csv('data.csv')
    wlength = list(df['Wavelength'])
    flux = list(df['Flux'])


    wlength = list(wlength)
    wwidth = width(wlength)
    chem = ['H-','O-','OH-']
    sigin_data = [1.0*10**-17,1.2*10**-17,3.3*10**-17]
    ea_data = [0.75,1.5,1.8]
    
    
    
    for i in range(3):
        
        csc = sigma(sigin_data[i],ea_data[i],wlength)
        
        k_rate = [x*y for x,y in zip(csc,flux)]

        
        height = [x/y for x,y in zip(k_rate,width(flux))]
        print('The total reaction rate is :',sum(k_rate),'s^-1')


        
        plt.xlim([0,20000])
        plt.yscale('log')
        plt.plot(wlength[:-1],height,'.')
        plt.title(chem[i]+' REACTION RATE')
        plt.xlabel('WAVELENGTH (A)')
        plt.ylabel('LOG RATE COEFFICIENT (s-1 A-1)')
        plt.savefig(chem[i]+'.png')
        plt.show()
        print('==========================')
    

    


if __name__ == '__main__':
    main()

# print(cal_csc(1100))
