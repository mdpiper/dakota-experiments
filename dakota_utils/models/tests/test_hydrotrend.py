#!/usr/bin/env python
#
# Tests for dakota_utils.models.hydrotrend.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from dakota_utils.models.hydrotrend import HydroTrend

def setup_module():
    print('HydroTrend tests:')
    os.environ['_test_hydrotrend_dir'] = tempfile.mkdtemp()
    os.chdir(os.environ['_test_hydrotrend_dir'])
    global h
    h = HydroTrend()

def teardown_module():
    shutil.rmtree(os.environ['_test_hydrotrend_dir'])

def test_HydroTrend_no_arguments():
    '''
    Tests whether no arguments creates input and output directories.
    '''
    assert_true(os.path.exists(h.input_dir))
    assert_true(os.path.exists(h.output_dir))

def test_HydroTrend_set_input_dir():
    '''
    Tests setting the input directory on init.
    '''
    os.chdir(os.environ['_test_hydrotrend_dir'])
    input_dir = '__hydro_in'
    h = HydroTrend(input_dir)
    assert_equal(h.input_dir, input_dir)

def test_HydroTrend_get_input_dir():
    '''
    Tests getting the input directory.
    '''
    input_dir = 'HYDRO_IN' # the default
    assert_equal(os.path.basename(h.input_dir), input_dir)

def test_HydroTrend_set_output_dir():
    '''
    Tests setting the output directory on init.
    '''
    os.chdir(os.environ['_test_hydrotrend_dir'])
    output_dir = '__hydro_out'
    h = HydroTrend(None, output_dir)
    assert_equal(h.output_dir, output_dir)

def test_HydroTrend_get_output_dir():
    '''
    Tests getting the output directory.
    '''
    output_dir = 'HYDRO_OUTPUT' # the default
    assert_equal(os.path.basename(h.output_dir), output_dir)

def test_HydroTrend_get_input_file():
    '''
    Tests getting the input file name.
    '''
    input_file = 'HYDRO.IN' # the default
    assert_equal(h.input_file, input_file)

def test_HydroTrend_set_input_file():
    '''
    Tests setting the input file name.
    '''
    input_file = '__hydro.in'
    h.input_file = input_file
    assert_equal(h.input_file, input_file)

def test_HydroTrend_get_input_template():
    '''
    Tests getting the input template name.
    '''
    input_template = 'HYDRO.IN.template' # the default
    assert_equal(h.input_template, input_template)

def test_HydroTrend_set_input_template():
    '''
    Tests setting the input template name.
    '''
    input_template = '__hydro.in.template'
    h.input_template = input_template
    assert_equal(h.input_template, input_template)

def test_HydroTrend_get_hypsometry_file():
    '''
    Tests getting the hypsometry file name.
    '''
    hypsometry_file = 'HYDRO0.HYPS' # the default
    assert_equal(h.hypsometry_file, hypsometry_file)

def test_HydroTrend_set_hypsometry_file():
    '''
    Tests setting the hypsometry file name.
    '''
    hypsometry_file = '__hydro0.hyps'
    h.hypsometry_file = hypsometry_file
    assert_equal(h.hypsometry_file, hypsometry_file)

def test_HydroTrend_get_output_files():
    '''
    Tests getting the tuple of output file names.
    '''
    output_files = ('HYDROASCII.QS') # the default
    assert_equal(h.output_files, output_files)

def test_HydroTrend_set_output_files():
    '''
    Tests setting the tuple of output file names.
    '''
    output_files = ('foo', 'bar', 'baz')
    h.output_files = output_files
    assert_equal(h.output_files, output_files)

def test_get_response_statistic():
    '''
    Tests getting the current response_statistic.
    '''
    rstat = 'mean' # the default
    assert_equal(h.response_statistic, rstat)

def test_set_response_statistic():
    '''
    Tests setting the response_statistic.
    '''
    rstat = 'sum'
    h.response_statistic = rstat
    assert_equal(h.response_statistic, rstat)

@raises(TypeError)
def test_load_zero_arguments():
    '''
    Tests load() when no argument is passed.
    '''
    r = h.load()

def test_load_does_not_exist():
    '''
    Tests load() when a nonexistent output file is defined.
    '''
    r = h.load('vfnqeubnuen.f')
    assert_is_none(r)



