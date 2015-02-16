#! /usr/bin/env python
# Analyzes output from Delft3D with MATLAB and communicates results to Dakota.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call

def main():
    '''
    Analyzes output from Delft3D with MATLAB and communicates results
    to Dakota.
    '''
    start_dir = os.path.dirname(os.path.realpath(__file__))
    cells_file = 'nesting.txt'
    analysis_program = 'total_sed_cal'
    analysis_program_file = analysis_program + '.m'
    analysis_results_file = analysis_program + '.out'

    # Call a MATLAB script to read the Delft3D output, calculate the
    # desired responses, and write the Dakota results file.
    shutil.copy(os.path.join(start_dir, cells_file), os.getcwd())
    shutil.copy(os.path.join(start_dir, analysis_program_file), os.getcwd())
    print('Current directory: ' + os.getcwd())
    matlab_cmd = '-r "' + analysis_program + '; exit"'
    r = call(['matlab', '-nodisplay', '-nosplash', matlab_cmd])
    print('MATLAB exit status code = ' + str(r))
    shutil.move(analysis_results_file, sys.argv[2])

if __name__ == '__main__':
    main()
