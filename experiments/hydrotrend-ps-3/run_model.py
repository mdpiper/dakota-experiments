#!/usr/bin/env python
# Brokers communication between Dakota and a model through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
import re
import importlib
from dakota_utils.read import get_analysis_component

def main():
    """Sets up model input, runs model, gathers output."""

    # Which model are we using?
    ac = get_analysis_component(sys.argv[1])
    try:
        m = importlib.import_module('dakota_utils.models.' + ac)
    except ImportError:
        raise

    if m.is_installed():
        h = m.model()
    else:
        print('Error: Model executable cannot be located.')
        return

    # The files and statistic used in the Dakota response.
    # TODO: How can I factor out these? Use additional analysis components?
    h.output_files = ('HYDROASCII.QS',)
    h.response_statistic = 'median'

    # References to files passed by Dakota.
    params_file = sys.argv[1]
    results_file = sys.argv[2]

    # Set up the model run, taking information from the parameters
    # file created by Dakota.
    start_dir = os.path.dirname(os.path.realpath(__file__))
    h.setup(start_dir, params_file)

    # Call the model, using the input file modified by Dakota.
    h.call()

    # Calculate the response statistic for the simulation. Write the
    # output to a Dakota results file.
    h.teardown(params_file, results_file)

if __name__ == '__main__':
    main()
