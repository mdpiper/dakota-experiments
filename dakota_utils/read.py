#! /usr/bin/env python
#
# Dakota utility programs for reading output.
#
# Mark Piper (mark.piper@colorado.edu)

import re
import numpy as np


def get_labels(params_file):
    '''
    Uses a regular expression to extract labels from a Dakota parameters file.
    '''
    labels = []
    try:
        with open(params_file, 'r') as fp:
            for line in fp:
                if re.search('ASV_', line):
                    labels.append(''.join(re.findall(':(\S+)', line)))
    except IOError:
        return None
    else:
        return(labels)


def get_analysis_components(params_file):
    """Extracts the analysis components from a Dakota parameters file.

    The components are returned as a list. The first item is the name
    of the model that's being examined by Dakota, followed by dicts
    containing the output file to analyze and the statistic to apply
    to the file. Note that this syntax is defined in the Dakota input
    file.

    Parameters
    ----------
    params_file : str
      The path to a Dakota parameters file.

    Returns
    -------
    list
      A list of analysis components for the Dakota experiment.

    Examples
    --------
    Extract the analysis components from a Dakota input file:

    >>> ac = get_analysis_components(params_file)
    >>> ac.pop(0)
    'hydrotrend'
    >>> ac.pop(0)
    {'file': 'HYDROASCII.QS', 'statistic': 'median'}

    Notes
    -----

    The syntax expected by this function is defined in the Dakota
    input file; e.g., for the example cited above, the 'interface'
    section of the Dakota input file contains the line:

      analysis_components = 'hydrotrend' 'HYDROASCII.QS:median'

    """
    ac = []
    try:
        with open(params_file, 'r') as fp:
            for line in fp:
                if re.search('AC_1', line):
                    ac.append(line.split('AC_1')[0].strip())
                elif re.search('AC_', line):
                    parts = re.split(':', re.split('AC_', line)[0])
                    ac.append({'file': parts[0].strip(),
                               'statistic': parts[1].strip()})
    except IOError:
        return None
    else:
        return(ac)


def get_names(dat_file):
    '''
    Reads the header from Dakota tabular graphics file. Returns a list
    of variable names or None on an error.
    '''
    try:
        with open(dat_file, 'r') as fp:
            names = fp.readline().split()
    except IOError:
        pass
    else:
        return names


def get_data(dat_file):
    '''
    Reads the data from Dakota tabular graphics file. Returns a numpy array.
    '''
    names = get_names(dat_file)
    rnames = range(len(names))
    rnames.pop(names.index('interface'))
    return np.loadtxt(dat_file, skiprows=1, unpack=True, usecols=rnames)


def read_tabular(dat_file):
    '''
    Reads a Dakota tabular graphics file. Returns a dict with variable
    names and a numpy array with data.
    '''
    names = get_names(dat_file)
    data = get_data(dat_file)
    return {'names': names, 'data': data}
