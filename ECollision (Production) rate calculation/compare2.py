import scipy as np
import matplotlib.pyplot as plt
# production DEA rates of cl
prodrCl = [8.04217401504*10**-17,
8.04217401504*10**-17,
8.04217401504*10**-17,
3.26309909003*10**-17,
3.26309909003*10**-17,
3.26309909003*10**-17,
8.83414486281*10**-17,
1.21136923603*10**-17,
]
# loss rates of Cl
lossrCl=[0.116,
0.116,
0.116,
0.00129,
0.00129,
0.00129,
0.000316,
0.005,]

# negative density
negativeD = [12,8,0.2,30,100,900,5*10**-2,5*10**-2]

# labels
labels = ['Earth 75km', 'Earth 65km','Earth 55km', 'Europa low e- density', 'Europa medium e- density','Europa high e- density',
          'commet halley (subject to change)', 'commet 77p (subject to change)']

# electron density
anions = [np.linspace(0,1),np.linspace(20,40),np.linspace(300,500),np.logspace(-2,3,10),np.logspace(-2,3,10),
           np.logspace(-2,3,10),np.logspace(-2,3,10),np.logspace(-2,3,10)]
neutral = np.logspace(-10, 20, num=10000)

import matplotlib.cm as cm

colors = cm.rainbow(np.linspace(0, 1, len(labels)))[::-1]

plt.figure(figsize=(20,16))
for i in range(len(prodrCl)):
   plt.rcParams['font.size'] = 20

   # CALCULATE  PRODUCTION & LOSS
   p = [prodrCl[i]*negativeD[i]*x for x in neutral]   # number of produced anions
   l = [lossrCl[i]*y for y in anions[i]]               # loss rates

   n_no = []
   a_no = []

   for j,_l in enumerate(l): # for each of the production rates
       for k,_p in enumerate(p):
           if _p >= _l:

               n_no.append(neutral[k])
               a_no.append(anions[i][j])
               break

       else:
           break
   print(labels[i],a_no,n_no,sep='\n')
   plt.loglog(a_no,n_no,label=labels[i],color=colors[i],linestyle='--')

plt.ylim([10**8,10**19])

plt.xlabel('Negative ion density ($cc$)')
plt.ylabel('Neutral density ($cc$)')
plt.title('Neutral density of $Cl_2$ based on ion density')
plt.legend()

plt.savefig('Across')
plt.show()