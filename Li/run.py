#!/usr/bin/env python
from Bands import *



datafile='Li.bands.dat.gnu'
fermi = 0.9767
symmetryfile='bands-pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black',linestyle='solid',name_k_points=['G',"N",'P','G',"H",'N'])

plt.ylim(-5,15)
#plt.title("NbSe2 No SOC")
fig.savefig("dft-bands.pdf")
plt.show()
