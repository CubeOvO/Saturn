from maxwell import *

chemical = ['O2O-','O-','OH-']


def main():
    print('___________________________')
    for j in range(len(chemical)):

        df = pd.read_csv(chemical[j]+'.csv')
        sigma = list(df['Csc'])
        energy = list(df['Energy'])
        vel = [en2vel(x*(1.6*10**-19)) for x in energy]

        krate = 0
        for i in range(len(vel)):
            if i:
                a = vel[i]*sigma[i]*maxwell(vel[i])*(vel[i]-vel[i-1])
                krate = krate + a
            else:
                a = vel[i]*sigma[i]*maxwell(vel[i])*(vel[i])
                krate = krate + a
        print('The rate constant for chemical {} is'.format(chemical[j]), krate*10**-18)
        print('___________________________')


if __name__ == '__main__':
    main()