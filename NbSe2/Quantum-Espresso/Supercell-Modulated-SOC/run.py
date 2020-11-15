#!/usr/bin/env python
from Bands import *

datafile='nbse2.bands.dat.gnu'
fermi = -0.4479
symmetryfile='3-bands_pp.out'
bool_shift_efermi= True
fig, ax = plt.subplots()

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(datafile,fermi,symmetryfile,ax,shift_fermi=-0.4479 ,\
color='black',linestyle='solid',name_k_points=['M','G','K','M'])

plt.ylim(-0.5,1)
plt.title("NbSe2 SOC 3x3 Modulated")
fig.savefig("soc-3x3-modulated.png")
plt.show()
