#!/usr/bin/python

import pickle
from datetime import datetime
from hash_fcns import *


# Prints the hash digests for all contents of a directory.
def checkHashDictonaryForDirectoryContents(directory, dictionary, dup_file, non_dup_file):
    dup = 0
    non_dup = 0
    total = 0
    for fileName, hashDigest in getHashDigestForDirectoryContents(directory):
        total = total + 1
        out = fileName + '\n'
        if hashDigest in dictionary:
            dup = dup + 1
            dup_file.write(out)
        else:
            non_dup = non_dup + 1
            non_dup_file.write(out)
    print "Total Files: %s" % total
    print "Duplicate Files: %s" % dup
    print "Non-Duplicate Files: %s" % non_dup


def processPathArgument(path):
    if not os.path.exists(path):
        print "Path doesn't exist: %s" % path
        raise ValueError('Invalid Path')
    return path


# Display command line usage information.
def usage():
    print "\nUsage: compare_against_dict.py <path> <dict-file> <dup-file> <non-dup-file>\n"

# Handles processing when run from the command line.
def main(args):
    try:
        path = processPathArgument(args[0])
        pkl = processPathArgument(args[1])
    except ValueError:
        usage()
        return

    dup_file = open(args[2], 'w')
    non_dup_file = open(args[3], 'w')

    pkl_file = open(pkl, 'rb')
    d = pickle.load(pkl_file)
    pkl_file.close()

    start = datetime.now();
    print "\nStarting: %s\n" % start
        
    checkHashDictonaryForDirectoryContents(path, d, dup_file, non_dup_file)
    
    
    finish = datetime.now()
    print "\nFinished: %s" % finish
    print "Total time: %s\n" % (finish - start)
    
    dup_file.close()
    non_dup_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        usage()
        sys.exit(2)

    try:
        main(sys.argv[1:])
    except (KeyboardInterrupt, SystemExit):
        print "Exiting..."

