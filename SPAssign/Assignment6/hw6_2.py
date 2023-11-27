#Using threading (10 threads) increment a counter from 0 to 1000000000 and print the result.
# it should decrement back to 0 and print the result.
# output:
#   Incrementing counter from 0 to 1000000000 using 10 threads
#   Final value is 1000000000
#   Decrementing counter from 1000000000 to 0 using 10 threads
#   Final value is 0

import threading
import sys

lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(1000000000):
        lock.acquire()
        counter += 1
        lock.release()
    print("Final value is " + str(counter))

def decrement():
    global counter
    for _ in range(1000000000):
        lock.acquire()
        counter -= 1
        lock.release()
    print("Final value is " + str(counter))

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hw6_2.py <counter value> <number of threads>")
        sys.exit(1)
    global counter
    counter = int(sys.argv[1])
    threads = []
    print("Incrementing counter from " + str(counter) + " to 1000000000 using " + sys.argv[2] + " threads")
    for i in range(int(sys.argv[2])):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    threads = []
    print("Decrementing counter from " + str(counter) + " to 0 using " + sys.argv[2] + " threads")
    for i in range(int(sys.argv[2])):
        t = threading.Thread(target=decrement)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    sys.exit(0)

if __name__ == "__main__":
    main()
