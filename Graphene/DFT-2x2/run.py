#!/usr/bin/env python
from Bands import *



datafile='graphene.bands.dat.gnu'
fermi = 4.8085
symmetryfile='bands-pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black',linestyle='solid',name_k_points=['K','G','M','K'])

plt.ylim(-10,15)
#plt.title("NbSe2 No SOC")
fig.savefig("dft-bands.pdf")
plt.show()
