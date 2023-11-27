#This program uses Popen to run "echo "Hello World" into a file and then uses Popen to run "cat" to read the file and print the contents to the screen.
# expected usage: python3 hw6_1.py

import sys
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hw6_1.py 'string' <filename>")
        sys.exit(1)
    # print "Using popen to echo 'string' to a file"
    print("Using popen to echo " + "'"+ sys.argv[1] + "'" + " to a file")
    # Using Popen to run "echo "string" into the created file"
    subprocess.Popen("echo " + sys.argv[1] + " > " + sys.argv[2], shell=True)
    # prints "Using popen to cat test.txt"
    print("Using popen to cat " + sys.argv[2] + "")
    # reads the contents of the file using Popen and print if the file exists and the command was successful
    if subprocess.Popen(sys.argv[2], shell=True):
        print(sys.argv[2] + " contains: " + sys.argv[1])
    else:
        print("File does not exist or command was unsuccessful")
    sys.exit(0)

if __name__ == "__main__":
    main()
