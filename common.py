#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Francesco Lumachi <francesco.lumachi@gmail.com>
''' Common operation of files. '''

import os

def appendSuffix(fname, suffix):
    ''' Append a specified suffix at the end of a file name but before extension
    '''
    return os.path.splitext(fname)[0] + suffix + os.path.splitext(fname)[1]
