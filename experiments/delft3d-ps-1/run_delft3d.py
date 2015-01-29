#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import shutil
from subprocess import call


def main():
    '''
    Brokers communication between Delft3D and Dakota through files.
    '''

    # Files and directories.
    input_template = 'WLD.sed.template'
    input_file = 'WLD.sed'

    # Use the parsing utility `dprepro` (from $DAKOTA_DIR/bin) to
    # substitute the parameters from Dakota into the input template,
    # creating a new Delft3D input file.
    call(['dprepro', sys.argv[1], input_template, input_file])

    # Call Delft3D, using the updated input file.
    call(['qsub', 'run_delft3d_wave.sh'])

    # Call a MATLAB script to read the Delft3D output, calculate the
    # desired responses, and write the Dakota results file.
    call(['matlab', '-nojvm', '-nodisplay', '-nosplash', '-r', \
          '"total_sed_cal; exit"'])
    shutil.move('results.out', sys.argv[2])

if __name__ == '__main__':
    main()
