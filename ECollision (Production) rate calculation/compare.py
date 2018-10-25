import scipy as np
import matplotlib.pyplot as plt

chem = ['O-','OH-','O2O-']
prodr = [6.8782,1.0321,0.41447]   # production rate, x10^-14
lossr = [0.0196,0.0108,0.00067]   # photodetachment rate at Saturn　ｓ－1
neutralRou = np.logspace(7, 12, num=10000)   # density of neutral particle
anions = np.logspace(-4, 2, num=10000)


for i in range(len(chem)):
   plt.figure(figsize=(9, 6))
   plt.rcParams['font.size'] = 14
   # CALCULATE  PRODUCTION & LOSS
   p = [prodr[i]*x*10**(-14) for x in neutralRou]   # number of produced anions
   l = [lossr[i]*y for y in anions]               # loss rates

   n_no = []
   a_no = []

   for j,_p in enumerate(p): # for each of the production rates
       for k,_l in enumerate(l):
           if _l >= _p:

               n_no.append(neutralRou[j])
               a_no.append(anions[k])
               break

       else:
           break
   plt.plot(a_no,n_no,)
   plt.show()
