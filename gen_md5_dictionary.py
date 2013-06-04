#!/usr/bin/python

import pickle
from datetime import datetime
from hash_fcns import *

# dictionary of hashes
d = {}

# Prints the hash digests for all contents of a directory.
def buildHashDictonaryForDirectoryContents(directory, dup_file, compare_file):
    total = 0
    dup = 0
    for fileName, hashDigest in getHashDigestForDirectoryContents(directory):
        total = total + 1
        if hashDigest in d:
            dup = dup + 1
            dup_file.write(fileName + '\n')
            compare_file.write(fileName + " " + dictionary[hashDigest] + '\n')
        else:
            addToHashDict(hashDigest, fileName)

def addToHashDict(key, value):
    d[key] = value;

def processPathArgument(path):
    if not os.path.exists(path):
        print "Path doesn't exist: %s" % path
        raise ValueError('Invalid Path')
    return path


# Display command line usage information.
def usage():
    print "\nUsage: gen_md5_dictionary.py <path> <file> <dup-file> <comp-file>\n"

# Handles processing when run from the command line.
def main(args):
    try:
        path = processPathArgument(args[0])
        filename = args[1]
    except ValueError:
        usage()
        return
        
    dup_file = open(args[2], 'w')
    compare_dup_file = open(args[3], 'w')
        

    start = datetime.now();
    print "\nStarting: %s\n" % start

    if os.path.isfile(path):
        print "Just a file!"
    else:
        buildHashDictonaryForDirectoryContents(path)
        
    output = open(filename, 'wb')
    pickle.dump(d, output)
    output.close()
    
    finish = datetime.now()
    print "\nFinished: %s" % finish
    print "Total time: %s\n" % (finish - start)

#    pkl_file = open(filename, 'rb')
#    dict_copy = pickle.load(pkl_file)
#    pkl_file.close()
#    print dict_copy


if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()
        sys.exit(2)

    try:
        main(sys.argv[1:])
    except (KeyboardInterrupt, SystemExit):
        print "Exiting..."

