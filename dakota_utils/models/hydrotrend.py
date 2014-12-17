#! /usr/bin/env python
#
# A module for working with HydroTrend.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import shutil
import subprocess
import numpy as np
from ..read import get_labels
from ..write import write_results


def is_installed():
    '''
    Returns True if the HydroTrend executable is in the path.
    '''
    try:
        subprocess.call(['hydrotrend', '--version'])
    except OSError:
        return False
    else:
        return True


class HydroTrend(object):
    '''
    Represents a HydroTrend simulation used in a Dakota experiment.
    '''
    def __init__(self, indir=None, outdir=None):
        '''
        Defines default files and directories.
        '''
        self._input_file = 'HYDRO.IN'
        self._input_template = 'HYDRO.IN.template'
        self._hypsometry_file = 'HYDRO0.HYPS'
        self._output_file = 'HYDROASCII.QS'

        # TODO: check permissions on directories
        self._input_dir = os.path.join(os.curdir, 'HYDRO_IN') \
                          if indir is None else indir
        if os.path.exists(self._input_dir) is False: 
            os.mkdir(self._input_dir, 0755)
        self._output_dir = os.path.join(os.curdir, 'HYDRO_OUTPUT') \
                           if outdir is None else outdir
        if os.path.exists(self._output_dir) is False: 
            os.mkdir(self._output_dir, 0755)

    @property
    def input_dir(self):
        '''
        HydroTrend input directory.
        '''
        return self._input_dir

    @input_dir.setter
    def input_dir(self, value):
        '''
        Sets HydroTrend input directory.
        '''
        self._input_dir = value

    @property
    def input_file(self):
        '''
        HydroTrend input file.
        '''
        return self._input_file

    @input_file.setter
    def input_file(self, value):
        '''
        Sets HydroTrend input file.
        '''
        self._input_file = value

    @property
    def input_template(self):
        '''
        A template HydroTrend input file used by Dakota.
        '''
        return self._input_template

    @input_template.setter
    def input_template(self, value):
        '''
        Sets the template HydroTrend input file used by Dakota.
        '''
        self._input_template = value

    @property
    def hypsometry_file(self):
        '''
        HydroTrend hypsometry file.
        '''
        return self._hypsometry_file

    @hypsometry_file.setter
    def hypsometry_file(self, value):
        '''
        Sets HydroTrend hypsometry file.
        '''
        self._hypsometry_file = value

    @property
    def output_dir(self):
        '''
        HydroTrend output directory.
        '''
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value):
        '''
        Sets HydroTrend output directory.
        '''
        self._output_dir = value

    @property
    def output_file(self):
        '''
        The HydroTrend output file selected for analysis.
        '''
        return self._output_file

    @output_file.setter
    def output_file(self, value):
        '''
        Sets the HydroTrend output file selected for analysis.
        '''
        self._output_file = value

    def setup(self, start_dir, params_file):
        '''
        Set up HydroTrend inputs. Use the Dakota parsing utility `dprepro`
        to incorporate parameters from Dakota into HydroTrend, creating a
        new input file.
        '''
        shutil.copy(os.path.join(start_dir, self._input_template), os.curdir)
        subprocess.call(['dprepro', params_file, \
                         self._input_template, \
                         self._input_file])
        shutil.copy(self._input_file, self._input_dir)
        shutil.copy(os.path.join(start_dir, self._hypsometry_file), \
                    self._input_dir)

    def call(self):
        '''
        Invokes HydroTrend through the shell.
        '''
        subprocess.call(['hydrotrend', \
                         '--in-dir', self._input_dir, \
                         '--out-dir', self._output_dir])

    def load(self):
        '''
        Reads a column of text containing HydroTrend output. Returns a
        numpy array, or None on an error.
        '''
        try:
            series = np.loadtxt(self._output_file, skiprows=2)
        except (IOError, StopIteration):
            pass
        else:
            return(series)

    def teardown(self, params_file, results_file):
        '''
        Reads HydroTrend output and calculates statistics to pass back to
        Dakota.
        '''
        shutil.copy(os.path.join(self._output_dir, self._output_file), \
                    os.curdir)
        labels = get_labels(params_file)
        series = self.load()
        if series is not None:
            m_series = [np.mean(series), np.std(series)]
        else:
            m_series = [float('nan'), float('nan')]
        write_results(results_file, m_series, labels)
