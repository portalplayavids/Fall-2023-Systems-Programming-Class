//Assignment: Signal Sychronization between Processes
//Objective: Implement signal synchronization between parent and child processes.

//signal mask:
//before calling Fork() in parent process, we need to block the signal

//signal handler:
//use the signal() func. to register a signal handler (signal_handler()) for sigusr1.
//should print out: "This is the signal handler!".

//Process Execution:
//parent process should print: "Parent started..."
//have parent sleep for 3 seconds.
//then print: "Parent about to signal child..."
//then send sigusr1 to child process.
//then exit parent

//child process:
//sig mask reset:
//first, replace the child process signal mask with an empty set. (allows for receiving of Sigusr1)
//wait for signal from parent.
//Sig receipt:
// upon receiving the signal, print: "Child received signal!"
//restore sig mask:
//restore the child process signal mask to its original value.

//exit:
//print: "Child exiting..."
//exit child process.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void signal_handler(int sig){
    printf("This is the signal handler!\n");
}

int main(){
    pid_t pid;
    sigset_t mask;
    sigemptyset(&mask);
    sigaddset(&mask, SIGUSR1);
    sigprocmask(SIG_BLOCK, &mask, NULL);
    signal(SIGUSR1, signal_handler);
    printf("Parent started...\n");
    sleep(3);
    printf("Parent about to signal child...\n");
    pid = fork();
    if(pid == 0){
        sigemptyset(&mask);
        sigaddset(&mask, SIGUSR1);
        sigprocmask(SIG_UNBLOCK, &mask, NULL);
        pause();
        printf("Child received signal!\n");
        sigprocmask(SIG_BLOCK, &mask, NULL);
        printf("Child exiting...\n");
        exit(0);
    }
    else{
        kill(pid, SIGUSR1);
        wait(NULL);
        printf("Parent exiting...\n");
        exit(0);
    }
    return 0;
}