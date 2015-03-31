#! /usr/bin/env python
#
# Tests for dakota_utils.read.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from dakota_utils.read import *

# Global variables
start_dir = os.getcwd()
data_dir = os.path.join(start_dir, 'dakota_utils', 'tests', 'data')
parameters_file = os.path.join(data_dir, 'params.in')
dat_file = os.path.join(data_dir, 'dakota.dat')
response_labels = ['Qs_median']
model = 'hydrotrend'
output_file = 'HYDROASCII.QS'
response_statistic = 'median'
dat_file_names = ['%eval_id', 'interface', 'T', 'P', 'Qs_median']

# Fixtures -------------------------------------------------------------

def setup_module():
    """Called before any tests are performed."""
    print('Read tests:')

def teardown_module():
    """Called after all tests have completed."""
    pass

# Tests ----------------------------------------------------------------

def test_get_labels():
    """Test the get_labels function."""
    assert_equal(response_labels, get_labels(parameters_file))

def test_get_labels_unknown_file():
    """Test get_labels() when parameters file not found."""
    assert_is_none(get_labels('foo.in'))

def test_get_analysis_components():
    """Test the get_analysis_components function."""
    ac = get_analysis_components(parameters_file)
    assert_equal(model, ac.pop(0))
    response = ac.pop(0)
    assert_equal(response['file'], output_file)
    assert_equal(response['statistic'], response_statistic)

def test_get_analysis_components_unknown_file():
    """Test get_analysis_components() when parameters file not found."""
    assert_is_none(get_analysis_components('foo.in'))

def test_get_names():
    """Test the get_names function."""
    assert_equal(dat_file_names, get_names(dat_file))

def test_get_data():
    """TODO: Test the get_data function."""
    pass

