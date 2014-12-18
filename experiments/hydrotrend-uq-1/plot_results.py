#!/usr/bin/env python
# Makes a standard set of plots from Dakota output.
# Mark Piper (mark.piper@colorado.edu)

# Note that these imports are from the installed version of dakota_utils.
from dakota_utils.read import read_tabular
from dakota_utils.plot import plot_samples, plot_irregular_surface
from dakota_utils.convert import has_interface_column, strip_interface_column

tab_file = 'dakota.dat'
if has_interface_column(tab_file):
    strip_interface_column(tab_file)
tab_data = read_tabular(tab_file)

plot_samples(tab_data, \
             outfile='dakota-hydrotrend-uq-1-lhs-samples.png')

plot_irregular_surface(tab_data, response_index=-2, \
                       title='HydroTrend: Mean Q(T,P)', \
                       outfile='dakota-hydrotrend-uq-1-Q_mean.png')

plot_irregular_surface(tab_data, response_index=-1, \
                       title='HydroTrend: Stdev Q(T,P)', \
                       outfile='dakota-hydrotrend-uq-1-Q_stdev.png')
