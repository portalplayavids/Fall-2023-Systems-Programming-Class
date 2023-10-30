#Assignment: Signal Synchronization between Processes
#Objective: Implement signal synchronization between parent and child processes.

import os
import signal
import time

def signal_handler(signum, frame):
    print("This is the signal handler!\n")

def child():
    signal.signal(signal.SIGUSR1, signal_handler)
    print("Child started...\n")
    time.sleep(3)
    print("Child about to signal parent...\n")
    os.kill(os.getppid(), signal.SIGUSR1)
    print("Child received signal!\n")
    exit()

def parent():
    signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGUSR1})
    signal.signal(signal.SIGUSR1, signal_handler)
    print("Parent started...\n")
    time.sleep(3)
    print("Parent about to signal child...\n")
    pid = os.fork()
    if pid == 0:
        child()
    else:
        os.waitpid(pid, 0)
        exit()


if __name__ == "__main__":
    parent()