#!/usr/bin/env python
from Bands import *

datafile='nbse2.bands.dat.gnu'
fermi = -1.6432
symmetryfile='bands-pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=fermi,\
color='black',linestyle='solid',name_k_points=['M','G','K','M'])
#plt.title("NbSe2 SOC")
plt.ylim(-10,3)
fig.savefig("soc-band.png")
plt.show()
