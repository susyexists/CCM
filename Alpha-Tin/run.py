#!/usr/bin/env python
from Bands import *



datafile='Sn.bands.dat.gnu'
fermi = 6.9723
symmetryfile='bands-pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black',linestyle='solid',name_k_points=['L','G','X'])

plt.ylim(-4,4)
#plt.title("NbSe2 No SOC")
fig.savefig("band.png")
plt.show()
