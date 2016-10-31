__author__ = 'ebirger'

import os
import glob
import sys

files = list()


def walk_files(search_path, depth):
    n = 1
    extra = '/*'
    while n <= int(depth):
        path = search_path + (extra * n)
        for i in glob.glob(path):
            files.append(os.path.join(path, i))
        n += 1

    so = sorted(files)
    separator = '--'
    up = u"\u2514"
    print os.path.basename(search_path)
    for i in so:
        intend = i.count(os.path.sep) - search_path.count(os.path.sep)
        print intend * '  ' + up.encode('utf-8') + separator + os.path.basename(i)


def main():
    walk_files(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print "Usage: tree.py <PATH> <DEPTH>"
        sys.exit(1)
    main()
