"""
Author: Matthew Rho
file: unpack.py
desc: A script to unpack student's files from mycourses
Given a mycourses zip file, unpack it, with all the student's files
All extra files given are ignored
"""

import zipfile, sys, os

"""
Where all the good stuff happens
"""
def main():
    argc = len(sys.argv)

    """
    Error checking, for you maniacs out there
    """
    if argc < 2: #not enough args
        print("usage: python %s file" % (sys.argv[0]), file=sys.stderr)
        exit(-1)

    if sys.argv[1][-4:] != ".zip": #ensure the file is a zip file
        print("file must be a zip file", file=sys.stderr)
        exit(-1)

"""
Run the main
"""
if __name__ == "__main__":
    main()