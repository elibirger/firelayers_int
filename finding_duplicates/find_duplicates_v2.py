__author__ = 'ebirger'


import os
import hashlib
import sys


f_names = dict()
dup_size = set()
crc = dict()
crc_dup = set()



def walk_files(search_path):
    for path, subdirs, files in os.walk(search_path):
        for name in files:
            filename = os.path.join(path, name)
            size = os.path.getsize(filename)
            if size in f_names:
                dup_size.add(size)
                f_names[size].append(filename)
            else:
                f_names.setdefault(size, [])
                f_names[size].append(filename)

def walk_sizes():
    for size in dup_size:
        for filename in f_names.get(size):

            md5 = hashlib.md5(open(filename, 'rb').read()).digest()
            if md5 in crc:
                crc_dup.add(md5)
                crc[md5].append(filename)
            else:
                crc.setdefault(md5, [])
                crc[md5].append(filename)

def print_dupies():
    for value in crc_dup:
        print crc.get(value)



def main():
    walk_files(sys.argv[1])
    walk_sizes()
    print_dupies()

if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: find_duplicates.py <PATH>"
        sys.exit(1)
    main()
