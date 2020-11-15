#!/usr/bin/env python
from Bands import *

datafile='nbse2.bands.dat.gnu'
fermi = -1.6254
symmetryfile='3-bands_pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=-1.5468 ,\
color='black',linestyle='solid',name_k_points=['M','G','K','M'])

plt.ylim(-0.5,1)
#plt.title("NbSe2 No SOC 3x3")
fig.savefig("3x3-nosoc-band.png")
plt.show()
