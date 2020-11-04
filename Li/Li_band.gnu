set style data dots
set nokey
set xrange [0: 7.34327]
set yrange [ -4.47901 : 21.45002]
set arrow from  1.29650,  -4.47901 to  1.29650,  21.45002 nohead
set arrow from  2.88439,  -4.47901 to  2.88439,  21.45002 nohead
set arrow from  3.80115,  -4.47901 to  3.80115,  21.45002 nohead
set arrow from  6.04676,  -4.47901 to  6.04676,  21.45002 nohead
set xtics ("G"  0.00000,"N"  1.29650,"P"  2.88439,"G"  3.80115,"H"  6.04676,"N"  7.34327)
 plot "Li_band.dat"
