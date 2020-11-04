set arrow from       1.29650315,     -4.47901096 to       1.29650315,     21.45002175 nohead
set arrow from       2.88438874,     -4.47901096 to       2.88438874,     21.45002175 nohead
set arrow from       3.80115491,     -4.47901096 to       3.80115491,     21.45002175 nohead
set arrow from       6.04676425,     -4.47901096 to       6.04676425,     21.45002175 nohead
set style data dots
unset key
set xrange [0: 7.34327]
set yrange [     -4.47901096 :     21.45002175]
set xtics (" G "  0.00000," N "  1.29650," P "  2.88439," G "  3.80115," H "  6.04676," N "  7.34327)
 plot "Li-bands.dat"
