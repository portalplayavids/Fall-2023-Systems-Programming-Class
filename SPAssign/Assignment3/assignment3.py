#!/usr/bin/env python3
# Elijah Guzman - nze594 - 09/24/2023
# Converting Assignment3.c to python

import os
import check_env

if __name__ == "__main__":  
    #Step 1: Set environment variable 'Assignment3' to 'best ever'
    os.environ["ASSIGNMENT3"] = "best ever"

    #Step 2: Get the process ID of the process
    pid = os.getpid()
    
    #   print("Process ID: ", pid) #Debugging

    #Step 3: Set environment variable 'PPID' to the parent process ID
    ppid = os.getppid() - 1
    PPID_STR = str(ppid)

    #   print("Parent Process ID: ", ppid) #Debugging

    os.environ["PPID"] = PPID_STR

    #   print("Environment Variable PPID: ", os.environ["PPID"]) #Debugging

    #Step 4: Set environment variable USER to "ee3233"
    os.environ["USER"] = "ee3233"

    #Call check_env.py to check environment variables
    check_env.check_environment_vars()
