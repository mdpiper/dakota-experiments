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
        self._output_files = ('HYDROASCII.QS')

        self._input_dir = os.path.join(os.curdir, 'HYDRO_IN') \
                          if indir is None else indir
        if os.path.exists(self._input_dir) is False: 
            os.mkdir(self._input_dir, 0755)
        self._output_dir = os.path.join(os.curdir, 'HYDRO_OUTPUT') \
                           if outdir is None else outdir
        if os.path.exists(self._output_dir) is False: 
            os.mkdir(self._output_dir, 0755)

        self._response_statistic = 'mean'

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
    def output_files(self):
        '''
        A tuple of HydroTrend output files selected for analysis.
        '''
        return self._output_files

    @output_files.setter
    def output_files(self, value):
        '''
        Sets the tuple of HydroTrend output files selected for analysis.
        '''
        self._output_files = value

    @property
    def response_statistic(self):
        '''
        A string setting the statistic used in the Dakota response. A
        choice of 'mean' (the default), 'stdev', 'sum', 'median', or 'max'.
        '''
        return self._response_statistic

    @response_statistic.setter
    def response_statistic(self, value):
        '''
        Sets the type of statistic used in the Dakota response.
        '''
        self._response_statistic = value

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

    def load(self, output_file):
        '''
        Reads a column of text containing HydroTrend output. Returns a
        numpy array, or None on an error.
        '''
        try:
            series = np.loadtxt(output_file, skiprows=2)
        except (IOError, StopIteration):
            pass
        else:
            return(series)

    def calculate(self):
        '''
        Calculates the statistic (sum, mean, ...) used in the Dakota
        response function.
        '''
        response = []
        for fname in self._output_files:
            shutil.copy(os.path.join(self._output_dir, fname), os.curdir)
            series = self.load(fname)
            if series is not None:
                if self._response_statistic == 'sum':
                    response.append(np.sum(series))
                elif self._response_statistic == 'std':
                    response.append(np.stdev(series))
                elif self._response_statistic == 'max':
                    response.append(np.max(series))
                elif self._response_statistic == 'median':
                    response.append(np.median(series))
                else:
                    response.append(np.mean(series)) # 'mean' is default
            else:
                response.append(float('nan'))
        return(response)

    def teardown(self, params_file, results_file):
        '''
        Reads HydroTrend output and calculates statistics to pass back to
        Dakota.
        '''
        response = self.calculate()
        labels = get_labels(params_file)
        write_results(results_file, response, labels)
