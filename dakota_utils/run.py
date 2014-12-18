#! /usr/bin/env python
#
# Runs Dakota experiments.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import subprocess
from glob import glob
import time


def is_dakota_installed():
    '''
    Returns True if Dakota is installed and in the execution path; 
    otherwise, False.
    '''
    try:
        subprocess.call(['dakota', '--version'])
    except OSError:
        return False
    else:
        return True


def get_input_file(experiment):
    '''
    Returns basename of Dakota input file, if present, or None.
    '''
    input_file = glob(os.path.join(experiment, '*.in'))
    if len(input_file) == 0:
        return None
    else:
        return os.path.basename(input_file[0])


def run_experiment(experiment):
    '''
    Performs the specified Dakota experiment.
    '''
    start_dir = os.getcwd()
    try:
        infile = get_input_file(experiment)
        outfile = os.path.splitext(infile)[0] + '.out'
        os.chdir(experiment)
        start_time = time.time()
        subprocess.check_output(['dakota', 
                                 '-i', infile, 
                                 '-o', outfile, 
                                 '-no_input_echo'], 
                                stderr=subprocess.STDOUT)
        elapsed_time = time.time() - start_time
    except AttributeError:
        status = 'Error: DAKOTA input file not found.'
    except subprocess.CalledProcessError as e:
        status = e
    else:
        status = 'Finished.\n%s %.1f %s' \
                 % ('Elapsed time:', elapsed_time, 's')
    finally:
        os.chdir(start_dir)
    return status


def print_error_status(error):
    '''
    Displays an error summary from Dakota on a failed run.
    '''
    print('Error: DAKOTA run failed.')    
    print('Command:\n' + '\t' + str(error.cmd))
    print('Return code:\n' + '\t' + str(error.returncode))
    print('Output:')
    for line in error.output.split('\n'):
        print('\t' + line)


def main():
    import argparse
    from dakota_utils import __version__, run_script

    parser = argparse.ArgumentParser(
        description="Runs a Dakota experiment on a CSDMS model.")
    parser.add_argument("experiment",
                        help="path to directory with Dakota experiment files")
    parser.add_argument('--version', action='version', 
                        version=run_script + ' ' + __version__)
    args = parser.parse_args()

    if is_dakota_installed() is False: 
        print('Error: DAKOTA must be installed and in the execution path.')
        return

    if os.path.isdir(args.experiment) is False:
        print('Error: Experiment path does not exist.')
        return
    else:
        print('Experiment: ' +
              os.path.basename(os.path.abspath(args.experiment)))

    status = run_experiment(args.experiment)
    if status.__class__ is subprocess.CalledProcessError:
        print_error_status(status)
    else:
        print(status)


if __name__ == '__main__':
    main()
