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
    if hydrotrend.is_installed() is False:
        print('Error: HydroTrend executable cannot be located.')
        return

    # References to files passed by Dakota.
    params_file = sys.argv[1]
    results_file = sys.argv[2]

    h = hydrotrend.HydroTrend()
    h.output_files = ('HYDROASCII.Q', 'HYDROASCII.QS', 'HYDROASCII.QB')

    # Set up the HydroTrend run, taking information from the parameters
    # file passed by Dakota.
    start_dir = os.path.dirname(os.path.realpath(__file__))
    h.setup(start_dir, params_file)

    # Call HydroTrend, using the input file modified by Dakota.
    h.call()

    # Calculate mean and standard deviation of a HydroTrend output time
    # series for the simulation. Write the output to a Dakota results file.
    h.teardown(params_file, results_file)


if __name__ == '__main__':
    main()
