#! /usr/bin/env python
#
# Cleans Dakota files.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import shutil
import glob


def remove_file(file):
    '''
    Deletes a file. Silently passes if the file doesn't exist.
    '''
    try:
        os.remove(file)
    except OSError:
        pass


def cleanup_experiment(experiment):
    '''
    Cleans up intermediate Dakota files after running an experiment.
    '''
    files = ['dakota.rst', 'run.log']
    for file in files:
        remove_file(os.path.join(experiment, file))
    for dir in glob.glob(os.path.join(experiment, 'step.*')):
        shutil.rmtree(dir)


def main():
    import argparse
    from utils import __version__, cleanup_script

    parser = argparse.ArgumentParser(
        description="Cleans up the results of a Dakota experiment.")
    parser.add_argument("experiment",
                        help="path to directory with Dakota experiment files")
    parser.add_argument('--version', action='version', 
                        version=cleanup_script + ' ' + __version__)
    args = parser.parse_args()

    if os.path.isdir(args.experiment) is False:
        print('Error: Experiment path does not exist.')
        return
    else:
        cleanup_experiment(args.experiment)

if __name__ == '__main__':
    main()
