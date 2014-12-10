#! /usr/bin/env python
#
# Tests for utils.dakota_utils.run.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from utils.dakota_utils.file import touch, remove
from utils.dakota_utils.run import *

def setup_module():
    print('Run tests:')
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

@raises(TypeError)
def test_no_experiment():
    '''
    Tests for no input parameter to run_experiment().
    '''
    run_experiment()

def test_no_experiment_content():
    '''
    Tests run_experiment() with nonexistent input file.
    '''
    err_str = 'Error: DAKOTA input file not found.'
    r = run_experiment(os.environ['_test_tmp_dir'])
    assert_equal(r, err_str)

def test_no_input_file():
    '''
    Tests get_input_file() for nonexistent input file.
    '''
    r = get_input_file(os.environ['_test_tmp_dir'])
    assert_is_none(r)

def test_has_input_file():
    '''
    Tests get_input_file() on an existing input file.
    '''
    input_file = 'dakota.in' # note '.in' extension
    full_input_file = os.path.join(os.environ['_test_tmp_dir'], input_file)
    touch(full_input_file)
    r = get_input_file(os.environ['_test_tmp_dir'])
    assert_equal(input_file, r)
    remove(full_input_file)
