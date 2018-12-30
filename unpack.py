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

def getname(mcstring):
    """
    Gets the name from the string of a mycourses format
    example: 110852-1506869 - Lastname, Firstname - lab01.zip
    The first and lastnames could have multiple spaces in them
    :param mcstring: The string with the student's name
    :return: A new string with just the last name and first name
    Note: the order will be last name, first name. The last name will have a comma after it
    """
    temp = mcstring.split()
    last = ""
    first = ""
    step = 0 #will determine what part of the name to assign
    for str in temp:
        if str == '-':
            step += 1
            continue

        if step == 1:
            last += str + ' '
            #The last name will have a comma at the end to sep from the firstname
            if str[-1] == ',':
                step += 1
                continue
        if step == 2:
            first += str + ' '
        #change what step we're at
    if step != 3:
        print("The file %s was of the incorrect format" % (mcstring), file=sys.stderr)
        return None

    last = last.strip()
    first = first.strip()
    return last + first

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
                sname = getname(file)
                if sname is None:
                    continue
                funzip(file, path=newdir, newname=sname)
                os.rename(file, newdir + '/' + sname + '/' + filename)
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