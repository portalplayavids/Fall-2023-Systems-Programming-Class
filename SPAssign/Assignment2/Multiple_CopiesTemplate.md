## Basic layout for Multiple_Copies.C

##### - Name

##### - pragma & Definitions

##### - Includes

##### - parameter initialization

- **copy_file function** 
```c
    2 inputs: (char* src, char* dst)
```
    - Declare pointers

    - initialize the source file handles

    - initialize the destination file handles

    - read the input source file handles

    - close the file handles

- **main function**
```c
    2 inputs: (int argc, char* argv[])
```
    - check to make sure the user had  provided the correct number of inputs

    - check to make sure the file exists

    - If the destination already exists, overwrite it

    - copy the contents of the source file to the destination

    - copy the contents of the source file to the second destination

To test the program 
create text file: `input.txt.`

Run: 

`gcc "program-name".c -o "build-file-name"`
    
     Note: build-file-name can be any name you'd like but its recommened
     to use the name of the program as the build file name 

Usage:

 ` ./"program-name".c <src file name> <dst 1 file name> <dst 2 file name>`