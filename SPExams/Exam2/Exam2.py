#!/usr/bin/env python3

#Use fork() to update /proc/sys/kernel/pid_max
#The Child process will read the old value, print it, and update the value to 5000000
#The Parent process will read the new value and print it

import os

def main():
    pid = os.fork()
    if pid == 0:
        #Child process
        f = open("/proc/sys/kernel/pid_max", "r")
        old = f.read()
        print("Old value: " + old)
        f.close()
        f = open("/proc/sys/kernel/pid_max", "w")
        f.write("5000000")
        f.close()
    else:
        #Parent process
        f = open("/proc/sys/kernel/pid_max", "r")
        new = f.read()
        print("New value: " + new)
        f.close()

if __name__ == "__main__":
    main()