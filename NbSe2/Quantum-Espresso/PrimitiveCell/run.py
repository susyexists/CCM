#!/usr/bin/env python
from Bands import *



datafile='nbse2.bands.dat.gnu'
fermi = -1.7489
symmetryfile='3-bands_pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black',linestyle='solid',name_k_points=['M','G','K','M'])

plt.ylim(-3,3)
#plt.title("NbSe2 No SOC")
fig.savefig("nosoc-band.png")
plt.show()
