import pylab as pl
import numpy as np
data = np.loadtxt('Li-bands.dat')
x=data[:,0]
y=data[:,1]
tick_labels=[]
tick_locs=[]
tick_labels.append('$\Gamma$')
tick_locs.append(0)
tick_labels.append(' N'.strip())
tick_locs.append(    1.296503)
tick_labels.append(' P'.strip())
tick_locs.append(    2.884389)
tick_labels.append('$\Gamma$')
tick_locs.append(    3.801155)
tick_labels.append(' H'.strip())
tick_locs.append(    6.046764)
tick_labels.append(' N'.strip())
tick_locs.append(    7.343267)
pl.scatter(x,y,color='k',marker='+',s=0.1)
pl.xlim([0,max(x)])
pl.ylim([min(y)-0.025*(max(y)-min(y)),max(y)+0.025*(max(y)-min(y))])
pl.xticks(tick_locs,tick_labels)
for n in range(1,len(tick_locs)):
   pl.plot([tick_locs[n],tick_locs[n]],[pl.ylim()[0],pl.ylim()[1]],color='gray',linestyle='-',linewidth=0.5)
pl.ylabel('Energy [eV]')
outfile = 'Li-bands.pdf'
pl.savefig(outfile,bbox_inches='tight')
pl.show()
