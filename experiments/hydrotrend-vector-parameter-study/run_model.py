#!/usr/bin/env python
# Brokers communication between Dakota and a model through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import importlib
from dakota_utils.read import get_analysis_components


def main():
    """Sets up model input, runs model, gathers output."""

    # Retrieve the analysis components passed through the Dakota input file.
    ac = get_analysis_components(sys.argv[1])
    model = ac.pop(0)
    response = ac.pop(0)

    # Which model are we using?
    try:
        m = importlib.import_module('dakota_utils.models.' + model)
    except ImportError:
        raise

    if m.is_installed():
        h = m.model()
    else:
        print('Error: Model executable cannot be located.')
        return

    # The files and statistic used in the Dakota response.
    h.output_files = (response['file'],)
    h.response_statistic = response['statistic']

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
