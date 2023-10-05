#Elijah Guzman - nze594 - 10/04/2023
#Assignment 4 - Perfom operations on files within a specified directory
#               based on provided arguments.
#Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]
#OUTPUT: (for <details> operation)
#       File: <filename><ext>
#       Permissions: <permissions>
#       Owner: <owner>
#       Group: <group>
#OUTPUT: (for <search> operation)
#       Keyword "<search_keyword>" found in: <filename><ext>

import os
import sys
#function to print the details of a file

def printDetails(file):
    #print file name
    print("File: " + file)
    #print file permissions
    print("Permissions: ", end = "")
    if os.access(file, os.R_OK):
        print("r", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.W_OK):
        print("w", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.X_OK):
        print("x", end = "")
    else:
        print("-", end = "")
    print(" ", end = "")
    if os.access(file, os.R_OK):
        print("r", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.W_OK):
        print("w", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.X_OK):
        print("x", end = "")
    else:
        print("-", end = "")
    print(" ", end = "")
    if os.access(file, os.R_OK):
        print("r", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.W_OK):
        print("w", end = "")
    else:
        print("-", end = "")
    if os.access(file, os.X_OK):
        print("x", end = "")
    else:
        print("-", end = "")
    print("")
    #print file owner
    print("Owner: " + str(os.stat(file).st_uid))
    #print file group
    print("Group: " + str(os.stat(file).st_gid))
    #print blank line
    print("")

#If <operation> is "details", print the details of all files in the specified directory.
def details(ext, directory):
    #print details of all files in directory
    for file in os.listdir(directory):
        if file.endswith(ext):
            printDetails(os.path.join(directory, file))

#If <operation> is "search", print the details of all files in the specified directory
#   that contain the <search_keyword> in their filename.
def search(ext, directory, search_keyword):
    #search for keyword in file names
    for file in os.listdir(directory):
        if file.endswith(ext):
            if search_keyword in file:
                print("Keyword \"" + search_keyword + "\" found in: " + os.path.join(directory, file))

#main function
def main():
    #check for correct number of arguments
    if len(sys.argv) < 4:
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct operation
    if sys.argv[1] != "details" and sys.argv[1] != "search":
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct extension
    if sys.argv[2][0] != ".":
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct directory
    if not os.path.isdir(sys.argv[3]):
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct number of arguments for search operation
    if sys.argv[1] == "search" and len(sys.argv) != 5:
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct number of arguments for details operation
    if sys.argv[1] == "details" and len(sys.argv) != 4:
        print("Usage: python3 Assignment_4.py <operation> <ext> <directory> [<search_keyword>]")
        return 1
    #check for correct number of arguments for search operation
    if sys.argv[1] == "search" and len(sys.argv) == 5:
        search(sys.argv[2], sys.argv[3], sys.argv[4])
    #check for correct number of arguments for details operation
    if sys.argv[1] == "details" and len(sys.argv) == 4:
        details(sys.argv[2], sys.argv[3])
    return 0

#call main function
if __name__ == "__main__":
    main()
