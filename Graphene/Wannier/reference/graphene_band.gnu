set style data dots
set nokey
set xrange [0: 4.01617]
set yrange [ -3.72232 : 17.15096]
set arrow from  1.69743,  -3.72232 to  1.69743,  17.15096 nohead
set arrow from  3.16745,  -3.72232 to  3.16745,  17.15096 nohead
set xtics ("K"  0.00000,"G"  1.69743,"M"  3.16745,"K"  4.01617)
 plot "graphene_band.dat"
