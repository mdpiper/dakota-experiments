#! /usr/bin/env python
#
# Tests for utils.dakota_utils.cleanup.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from utils.dakota_utils.cleanup import *

def setup_module():
    print('Cleanup tests:')
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

@raises(TypeError)
def test_no_experiment():
    '''
    Tests for no input parameter to cleanup_experiment().
    '''
    cleanup_experiment()

def test_empty_experiment():
    '''
    Tests cleanup_experiment() on an empty experiment directory.
    '''
    cleanup_experiment(os.environ['_test_tmp_dir'])

