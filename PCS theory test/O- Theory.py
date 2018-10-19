from h_theory import *

def rytoans(a):
    # change photon in ry to its corresponding wavelength
    b = []
    for i in a:
        b.append(10**10*6.63*10**-34*3.0*10**8/(i*13.6*1.6*10**-19))
    return b



def main():
    df = pd.read_csv('-veioncsc.csv')  # read data
    wlength = list(df['0'])
    crosss = list(df['2'])

    en = length_ev(rytoans([x+0.1077 for x in wlength]))  # convert to energy

    plotsigma(1.2 * 10 ** -17, 1.5, en)  # plot graph for theory

    cross = [x * 10 ** -18 for x in crosss]
    w = width(wlength)
    plt.plot(en[:-1], cross[:-1], '.')  # plot graph for data
    plt.savefig('o')
    plt.show()
    var(1.2 * 10 ** -17, 1.5, en)  # variance


if __name__ == '__main__':
    main()
