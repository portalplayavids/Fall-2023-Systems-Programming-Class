#Create a python3 script, with a main() entry point, that will:
#Create five threads to divide a workload into five equal parts.
#The script must include a global list (glist) that is initialized with all the numbers from 0 to 499.
#Then, each thread will be given as a target in accumulate(i: int) function, where the i argument depicts
#a starting index that the function will use to identify its workload.

#The accumulate(i: int) function will:
#Add all the numbers from the global list (glist) and put the result in a local acc variable.

#To make acc available to other threads, the function will use a global list (acc_list) to store the result.
#   acc_list = [0] * 5
#   acc_list[i] = acc

#Once all the threads have finished, the main() function will add all the numbers from the acc_list and print the result.

#To Monitor the execution of the script, the main() function will print the following messages:
#   print(f"Accumulated value in thread [{tid} -> {i}] is {acc_list[i]}")

#tid is the thread id. To retrieve it, use:
#   tid = threading.get_ident() 
#unless you're using a VM, in which case you should use:
#   tid = threading.get_native_id()

#In the main thread, print the following message:
#   print(f"Total is: {total}")
#where total is the sum of all the numbers from the acc_list[i] + acc+list[2] + acc_list[3] + acc_list[4]...

#To run the script, use:
#   python3 acc_elijah_guzman.py


import threading
import time

glist = list(range(500))
acc_list = [0] * 5


def accumulate(i: int):
    global glist
    global acc_list
    acc = 0
    for x in glist[i:i+99]:
        acc += x
    acc_list[i] = acc
    tid = threading.get_ident()
    print(f"Accumulated value in thread [{tid} -> {i}] is {acc}")

if __name__ == "__main__":
    threads = []
    max_threads = 5
    for i in range(max_threads):
        t = threading.Thread(target=accumulate, args=(i,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    total = 0
    total += acc_list[0] + acc_list[1] + acc_list[2] + acc_list[3] + acc_list[4]
    print(f"Total is: {total}")