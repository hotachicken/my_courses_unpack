"""
Author: Matthew Rho
file: unpack.py
desc: A script to unpack student's files from mycourses
Given a mycourses zip file, unpack it, with all the student's files
All extra files given are ignored
"""

import zipfile, sys, os
CWD = os.getcwd()

def funzip(file):
    """
    Unzip a file and put it into a folder of the same name
    :param file: str, file to be unzipped
    :return: None
    """
    flen = len(file) #file length
    ploc = flen - 4 #location of period in '.zip'

    os.mkdir(CWD + '/' + file[:ploc])
    with zipfile.ZipFile(file, 'r') as zip:
        zip.printdir()
        zip.extractall()

def main():
    """
    Where all the good stuff happens
    :return: None
    """
    argc = len(sys.argv)
    """
    Error checking, for you maniacs out there
    """
    if argc < 2: #not enough args
        print("usage: python %s file" % (sys.argv[0]), file=sys.stderr)
        exit(-1)

    filename = sys.argv[1]
    if len(filename) < 5:
        print("The length of the file was not long enough", file=sys.stderr)

    if filename[-4:] != ".zip": #ensure the file is a zip file
        print("file must be a zip file", file=sys.stderr)
        exit(-1)

    try:
        funzip(filename)
    except:
        print("An error occured", file=sys.stderr)
        exit(-1)
"""
Run the main
"""
if __name__ == "__main__":
    main()