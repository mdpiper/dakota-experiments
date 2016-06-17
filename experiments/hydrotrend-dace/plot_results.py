#!/usr/bin/env python
# Makes a standard set of plots from Dakota output.
# Mark Piper (mark.piper@colorado.edu)

# Note that these imports are from the installed version of dakota_utils.
from dakota_utils.read import read_tabular
from dakota_utils.plot import plot_samples, plot_irregular_surface

tab_file = 'dakota.dat'
tab_data = read_tabular(tab_file)

plot_samples(tab_data, \
             outfile='dakota-hydrotrend-dace-1-lhs-samples.png')

plot_irregular_surface(tab_data, response_index=-2, \
                       title='HydroTrend: Mean Qs(T,P)', \
                       outfile='dakota-hydrotrend-dace-1-Qs_mean.png')

plot_irregular_surface(tab_data, response_index=-1, \
                       title='HydroTrend: Stdev Qs(T,P)', \
                       outfile='dakota-hydrotrend-dace-1-Qs_stdev.png')
