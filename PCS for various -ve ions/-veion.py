import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import flux
df = pd.read_csv('data.csv')
wlength = list(df['Wavelength'])
flux = list(df['Flux'])

chem = ['C-','O-','F-','Si-','S-','Cl-','Br-','I-',]
# import csc
df1 = pd.read_csv('-veioncsc.csv')
potential = list(df1[str(9)])


def rytoans(a):
    # change photon in ry to its corresponding wavelength
    b = []
    for i in a:
        b.append(10**10*6.63*10**-34*3.0*10**8/(i*13.6*1.6*10**-19))
    return b


# estimate a given cross-section using data provided
def cal_csc(wlengthi,j):
    # process given wavelength
    photonE = df1[str(0)]-np.ones(len(df1[str(0)]))*potential[j]
    clength = list(rytoans(photonE))
    clength = list(reversed(clength))
    csc =list(reversed(df1[str(j+1)]))
    l,r = 0,0

    # find the position of the given wavelength
    for i in range(len(clength)):
        # print(wlengthi)
        # print(clength[i])
        if(clength[i]>=wlengthi):
            l, r = i - 1, i
            break
        pass

    # if exceed max interplot wavelength
    if not (l or r):
        # print('out of reach!')
        return 0
    # interplot wavelength
    else:
        grad = (csc[r]-csc[l])/(clength[r]-clength[l])
        return csc[l]+grad*(wlengthi-clength[l])
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


data1 = []
# for every chemical
for j in range(8):
    print('This is chemical {}'.format(chem[j]))

    # calcultae the range of freq provided
    photonE = df1[str(0)] - np.ones(len(df1[str(0)])) * potential[j]
    clength = list(rytoans(photonE))
    clength = list(reversed(clength))
    print('Range of wavelength avaliable: {}~{}'.format(clength[0],clength[-1]))
    wlength = list(wlength)
    wwidth = width(wlength)

    # process k_rate and its density
    k_rate = []
    height = []
    for i in range(len(wlength)-1):
        k = flux[i]*cal_csc(wlength[i],j)
        k_rate.append(k*(10**-18))
        height.append(k*(10**-18)/wwidth[i])

    # plot k_rate density
    plt.yscale('log')
    plt.xlim([0,20000])
    plt.ylim([10e-11,10e-3])
    plt.plot(wlength[:-43],height[:-42])
    ac_k_rate = sum(k_rate)*0.17/14

    # output data
    print('The total reaction rate of {} at Earth is : {}'.format(chem[j],sum(k_rate)))
    print('At Enceladus, it rate would be {:.2}, giving a half life of {:5.4} sec'.format(ac_k_rate,1/ac_k_rate))
    print('------------')
    plt.show()

    data1.append([chem[j],clength[-1],ac_k_rate,1/ac_k_rate])

# print summary
print('chemical:longest wavelength:::::rxn rate:::::::::half-life')
for data in data1:
    print(data)