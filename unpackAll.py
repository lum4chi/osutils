#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Francesco Lumachi <francesco.lumachi@gmail.com>

import tarfile, os, getopt, sys
''' Unzippa file multipli a partire dalla directory da cui è chiamato lo script.
    I files sono decompressi allo stesso livello del file compresso.
'''

def unpack_GZ(path, tname):
    tpathname = os.path.join(path, tname)
    tfile = tarfile.open(tpathname, 'r:gz')
    members = tfile.getmembers()
    # Per ogni file, appiattisci la directory di decompressione
    for m in members:
        m.name = os.path.basename(m.name)
    tfile.extractall(path)
    tfile.close()

# Default
delete_unpacked = False

# Leggi argparse
opts, _ = getopt.getopt(sys.argv[1:], "d", ['delete'])
for opt, arg in opts:
    if opt=='-d': delete_unpacked = True

# Cerca tutti i files
for path, _, files in os.walk('.'):
    # Filtra solo i .gz
    tarfiles = [f for f in files if os.path.splitext(f)[1] == '.gz']
    for tname in tarfiles:
        print 'Unpacking {}'.format(os.path.join(path, tname))
        unpack_GZ(path, tname)
        if delete_unpacked:
            print 'Deleting {}'.format(os.path.join(path, tname))
            os.remove(os.path.join(path, tname))
print 'Fatto!'
