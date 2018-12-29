"""
Author: Matthew Rho
file: unpack.py
desc: A script to unpack student's files from mycourses
Given a mycourses zip file, unpack it, with all the student's files
All extra files given are ignored
"""

import zipfile, sys, os
CWD = os.getcwd()

def funzip(file, newname=None):
    """
    Unzip a file and put it into a folder of the same name
    :param file: str, file to be unzipped
    :return: str, the new directory
    """
    flen = len(file) #file length
    ploc = flen - 4 #location of period in '.zip'

    #we want to rename the file to something other than the folder name
    if newname is not None:
        os.mkdir(CWD + '/' + newname)
        newdir = CWD + '/' + newname
    else:
        os.mkdir(CWD + '/' + file[:ploc])
        newdir = CWD + '/' + file[:ploc]
    with zipfile.ZipFile(file, 'r') as zip:
        zip.printdir()
        zip.extractall(path=newdir)
    return newdir

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

    #mycourses file we are going to unzip
    filename = sys.argv[1]
    print(filename)
    if len(filename) < 5:
        print("The length of the file was not long enough", file=sys.stderr)
        print('In the case that the file has spaces in it,\
         wrap the name with double quotes (") please', file=sys.stderr)
        exit(-1)

    if filename[-4:] != ".zip": #ensure the file is a zip file
        print("file must be a zip file", file=sys.stderr)
        exit(-1)

    #Unzip the first file
    try:
        newdir = funzip(filename)

        #unzip everything else
        for file in newdir:
            if file[-4:] == ".zip":
                #TODO strip the numbers off the student's zip files
                funzip(file)
    except:
        print("An error occured", file=sys.stderr)
        exit(-1)

"""
Run the main
"""
if __name__ == "__main__":
    main()