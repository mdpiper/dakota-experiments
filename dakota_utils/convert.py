#! /usr/bin/env python
#
# Dakota utility programs for converting output.
#
# Mark Piper (mark.piper@colorado.edu)

import shutil
from subprocess import check_call, CalledProcessError
from .read import get_names


def has_interface_column(tab_file):
    '''
    Returns True if the tabular output file has the v6.1 'interface' column.
    '''
    try:
        val = get_names(tab_file)[1] == 'interface'
    except IOError:
        raise
    else:
        return(val)


def strip_interface_column(tab_file):
    '''
    Strips the 'interface' column from a Dakota 6.1 tabular output file.
    '''
    try:
        bak_file = tab_file + '.orig'
        shutil.copyfile(tab_file, bak_file)
        cmd = 'cat ' + bak_file +' | colrm 9 18 > ' + tab_file
        check_call(cmd, shell=True)
    except (IOError, CalledProcessError):
        raise


def main():
    import argparse
    from dakota_utils import __version__, convert_script

    parser = argparse.ArgumentParser(
        description="Converts a Dakota tabular output file to v6.0 format.")
    parser.add_argument("output_file",
                        help="path to a Dakota v6.1 tabular output file")
    parser.add_argument('--version', action='version', 
                        version=convert_script + ' ' + __version__)
    args = parser.parse_args()

    if has_interface_column(args.output_file) is False:
        print('Error: Not a Dakota v6.1 tabular output file.')
        return
    else:
        strip_interface_column(args.output_file)


if __name__ == '__main__':
    main()
