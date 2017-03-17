import Gnuplot

g = Gnuplot.Gnuplot()
g('set datafile separator ","')
g('set term eps enhanced font "Arial, 20"')
g('set grid ytics lt 1 lc "gray"')
g.xlabel('Pressure (psi)')
g.ylabel('Measurement (mm)')
g('set out "rs.eps"')
#g('unset key')
g('f(x) = a*x + b')
g('fit f(x) "rs.csv" u 1:2 via a, b')
g('title_f(a,b) = sprintf(\'%.2fx + %.2f\', a, b)')
g('set xrange [90:260]')
#g('set yrange [0:25]')
g('plot "rs.csv" using 1:2 with points pt 7 lc 7 title "", f(x) t title_f(a,b) lt 2 lc 8 lw 3')
