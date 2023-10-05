## EE 3233 Systems Programming for Engineers (Fall 2023)

### Programming Assignment 3 (Python/C)

#### Objective:
Write a program in Python or C that performs operations on files within a specified directory based on provided arguments.

(lecture 6 has some examples that might be useful)

#### Usage:

##### For Python:
```Python
$ python3 yourname_hw3.py <operation> <ext> <directory> [<search_keyword>]
```

##### For C:
```C
$ ./yourname_hw3 <operation> <ext> <directory> [<search_keyword>]
```

### Instructions:

Operation: The type of operation you want the program to perform ("details" or "search").

Ext: The file extension to filter by within the specified directory.

Directory: The directory where the operation will be performed.

Search Keyword: (Optional) A keyword to search for within the files. Required if Operation is "search".

### Tasks:

[25 points] 

#### A. Details Operation:
If Operation is "details", the program will display the following details for all files with the specified extension in the given directory:

```
File permissions
Username of the file owner
Group name of the file owner
File name
```

[25 points]

#### B. Search Operation:
If Operation is "search", the program will search within the files with the specified extension in the given directory for the provided search keyword. It will then print the names of the files that contain the search keyword.

# Examples:

## Details Operation:

Suppose there are two files in the directory:

```$/home/user/documents```

```md
- report.txt
- notes.txt
```
The user wants to see the details of all .txt files
in that directory.


#### Command:

##### For Python:
```Bash
 $ python3 yourname_hw3.py details .txt /home/user/documents
```
##### For C:
```Bash
$ ./yourname_hw3 details .txt /home/user/documents
```

### Output:

```Bash
    File: report.txt
    Permissions: 755
    Owner: user
    Group: usergroup

    File: notes.txt
    Permissions: 644
    Owner: user
    Group: usergroup
```

## Search Operation:
In the same directory:
```/home/user/documents``` with files 
```md
-- notes.txt
```
 report.txt 
the user wants to search for the keyword "meeting" in all .txt files.

### Command:
##### For Python: 
```Bash
$ python3 yourname_hw3.py search .txt /home/user/documents meeting
```

##### For C: 
```Bash
$ ./yourname_hw3 search .txt /home/user/documents meeting
```

### Output: 
```Bash
Keyword "meeting" found in: notes.txt
```