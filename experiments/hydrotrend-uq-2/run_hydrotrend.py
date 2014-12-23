#!/usr/bin/env python
# Brokers communication between HydroTrend and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
from dakota_utils.models import hydrotrend


def main():
    '''
    Sets up HydroTrend input, runs model, gathers output. 
    '''
    if hydrotrend.is_installed():
        h = hydrotrend.HydroTrend()
    else:
        print('Error: HydroTrend executable cannot be located.')
        return

    # The files and statistic used in the Dakota response.
    h.output_files = ('HYDROASCII.QS',)
    h.response_statistic = 'median'

    # References to files passed by Dakota.
    params_file = sys.argv[1]
    results_file = sys.argv[2]

    # Set up the HydroTrend run, taking information from the parameters
    # file created by Dakota.
    start_dir = os.path.dirname(os.path.realpath(__file__))
    h.setup(start_dir, params_file)

    # Call HydroTrend, using the input file modified by Dakota.
    h.call()

    # Calculate mean and standard deviation of a HydroTrend output time
    # series for the simulation. Write the output to a Dakota results file.
    h.teardown(params_file, results_file)


if __name__ == '__main__':
    main()
