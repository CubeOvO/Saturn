import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


T = 15459*100 # 2eV
me = 9.11*10**-31
pi = np.pi
kb = 1.38*10**-23


def vel2en(v):
    return 0.5*me*v**2


def en2vel(e):
    return np.sqrt(2*e/me)


def alpha(temp):
    return me/(2*kb*temp)


def a(temp):
    return np.sqrt(me/(2*pi*kb*temp))


def maxwell(v):
    return a(T)**3*4*pi*v**2*np.exp(-alpha(T)*v**2)


def main():

    velocity = np.linspace(1, 2 * 10 ** 6, 10000)  # change this only

    energy = [vel2en(x) / (1.6 * 10 ** -19) for x in velocity]
    probability = [maxwell(x) for x in velocity]
    plt.plot(energy, probability)

    print(energy[100:], energy[:100], sep='\n')
    plt.xlabel('Energy (eV)')
    plt.ylabel('Relative Probability')
    plt.savefig('maxwell.png')
    plt.show()


if __name__ == '__main__':
    main()