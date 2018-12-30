"""
Author: Matthew Rho
file: unpack.py
desc: A script to unpack student's files from mycourses
Given a mycourses zip file, unpack it, with all the student's files
All extra files given are ignored
"""

import zipfile, sys, os
CWD = os.getcwd()

def funzip(file, path=CWD,  newname=None):
    """
    Unzip a file and put it into a folder of the same name
    :param file: str, file to be unzipped
    :return: str, the new directory
    """
    flen = len(file) #file length
    ploc = flen - 4 #location of period in '.zip'

    #we want to rename the file to something other than the folder name
    if newname is not None:
        os.mkdir(path + '/' + newname)
        newdir = path + '/' + newname
    else:
        os.mkdir(path + '/' + file[:ploc])
        newdir = path + '/' + file[:ploc]
    with zipfile.ZipFile(file, 'r') as zip:
        #zip.printdir()
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
    #print(filename)
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
        #print(newdir)
        #go to new directory
        os.chdir(newdir)
        dirlst = os.listdir(newdir)
        #unzip everything else
        for file in dirlst:
            print(file)
            if file[-4:] == ".zip":
                temp = file.split()
                if len(temp) != 6:
                    print("file %s was of the incorrect format" % (file), file=sys.stderr)
                    continue
                sname = temp[2] + temp[3] #student name
                funzip(file, path=newdir, newname=sname)
                os.rename(file, newdir + '/' + sname)
        #go back to old directory
        os.chdir(CWD)
    except OSError:
        print("File already exists", file=sys.stderr)
        exit(-1)
    except:
        print("A general error occurred", file=sys.stderr)
        exit(-1)

"""
Run the main
"""
if __name__ == "__main__":
    main()