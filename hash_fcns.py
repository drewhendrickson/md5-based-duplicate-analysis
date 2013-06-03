#!/usr/bin/python

import sys
import os
import hashlib

# Returns the hash digest for a file in hex format.
# Set blockSize to adjust size of data read in and hashed while
# processing the file.
def getHashDigestForFile(fileName, blockSize=2**8):
    try:
        f = open(fileName,'rb')
        h = hashlib.new('md5')
        while True:
            data = f.read(blockSize)
            if not data:
                break
            h.update(data)
        f.close()
        return h.hexdigest()
    except:
        print "    *******    Error opening file! %s *******    " % fileName
        return 0

# Generator function to return a tuple containing the file name (with
# path) and the hash digest for all contents of a directory.
def getHashDigestForDirectoryContents(directory):
    for baseDir, dirs, files in os.walk(directory):
        for file in files:
            fileName = os.path.join(baseDir, file)
            yield (fileName, getHashDigestForFile(fileName))

