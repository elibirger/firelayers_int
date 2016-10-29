__author__ = 'ebirger'


import os
import hashlib
import sys


f_names = dict()
dupies = set()


def walk_files(search_path):
    for path, subdirs, files in os.walk(search_path):
        for name in files:
            filename = os.path.join(path, name)
            md5 = hashlib.md5(open(filename, 'rb').read()).digest()
            if md5 in f_names:
                dupies.add(md5)
                f_names[md5].append(filename)
            else:
                f_names.setdefault(md5, [])
                f_names[md5].append(filename)


def print_dupies():
    for value in dupies:
        print f_names.get(value)


def main():
    walk_files(sys.argv[1])
    print_dupies()

if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: find_duplicates.py <PATH>"
        sys.exit(1)
    main()


