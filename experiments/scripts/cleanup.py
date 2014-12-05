#! /usr/bin/env python
#
# Cleans Dakota files.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import shutil
import glob

os.remove('dakota.rst')
os.remove('run.log')
for dir in glob.glob('step.*'):
    shutil.rmtree(dir)
