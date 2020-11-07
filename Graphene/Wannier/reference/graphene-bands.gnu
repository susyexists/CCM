set arrow from       1.69743347,     -3.72231618 to       1.69743347,     17.15095927 nohead
set arrow from       3.16745400,     -3.72231618 to       3.16745400,     17.15095927 nohead
set style data dots
unset key
set xrange [0: 4.01617]
set yrange [     -3.72231618 :     17.15095927]
set xtics (" K "  0.00000," G "  1.69743," M "  3.16745," K "  4.01617)
 plot "graphene-bands.dat"
