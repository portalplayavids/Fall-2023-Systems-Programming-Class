#Using threading and multiprocessing (10 threads) increment a counter from 0 to 1000000000 and print the result.
# it should decrement back to 0 and print the result.
# output:
#   Incrementing counter from 0 to 1000000000 using 10 threads
#   Final value is 1000000000
#   Decrementing counter from 1000000000 to 0 using 10 threads
#   Final value is 0

import threading
import sys
import multiprocessing

from multiprocessing import Process, Lock
import os

def increment(counter):
    for _ in range(1000000000):
        with counter.get_lock():
            counter.value += 1
    print("Final value is " + str(counter.value))

def decrement(counter):
    for _ in range(1000000000):
        with counter.get_lock():
            counter.value -= 1
    print("Final value is " + str(counter.value))

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hw6_3.py <counter value> <number of threads>")
        sys.exit(1)
    counter = multiprocessing.Value('i', int(sys.argv[1]))
    processes = []
    print("Incrementing counter from " + str(counter) + " to 1000000000 using " + sys.argv[2] + " threads")
    for i in range(int(sys.argv[2])):
        p = Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    processes = []
    print("Decrementing counter from " + str(counter) + " to 0 using " + sys.argv[2] + " threads")
    for i in range(int(sys.argv[2])):
        p = Process(target=decrement, args=(counter,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    sys.exit(0)

if __name__ == "__main__":
    main()