#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call
import numpy as np

def main():

    print('In run_delft3d.main()')

    # Files and directories.
    # start_dir = os.path.dirname(os.path.realpath(__file__))
    # input_dir = os.path.join(start_dir, 'HYDRO_IN')
    # if not os.path.exists(input_dir): os.mkdir(input_dir)
    # output_dir = os.path.join(start_dir, 'HYDRO_OUTPUT')
    # if not os.path.exists(output_dir): os.mkdir(output_dir)
    # input_template = 'HYDRO.IN.template'
    # input_file = 'HYDRO.IN'
    # output_file = 'HYDROASCII.QS'

    # Use the parsing utility `dprepro` (from $DAKOTA_DIR/bin) to
    # incorporate the parameters from Dakota into the HydroTrend input
    # template, creating a new HydroTrend input file.
    # shutil.copy(os.path.join(start_dir, input_template), os.curdir)
    # call(['dprepro', sys.argv[1], input_template, input_file])
    # shutil.copy(input_file, input_dir)

    # Call HydroTrend, using the updated input file.
    # call(['hydrotrend', '--in-dir', input_dir, '--out-dir', output_dir])

    # Calculate mean and standard deviation of a HydroTrend output time
    # series for the simulation. Write the output to a Dakota results file.
    # shutil.copy(os.path.join(output_dir, output_file), os.curdir)
    # labels = get_labels(sys.argv[1])
    # series = read(output_file)
    # if series != None:
    #     m_series = [np.mean(series), np.std(series)]
    # else:
    #     m_series = [float('nan'), float('nan')]
    # write_results(sys.argv[2], m_series, labels)


if __name__ == '__main__':
    main()
