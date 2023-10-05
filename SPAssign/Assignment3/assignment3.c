#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void check_code();

int main()
{
    // Step 1
    // set environment variable ASSIGNMENT3 to "best ever"
    setenv("ASSIGNMENT3", "best ever", 1);

    // Step 2
    // write code to get your process's PID
    // NOTE: the pid is of type pid_t (int for our case)
    // example code to convert int to char[]
    // char pid_str[8] = {0};
    // sprintf(pid_str, "%d", <variable used for getpid>);

    pid_t pid = getpid();
     printf("pid: %d\n", pid); // for debugging

    // Step 3
    // set environment variable PPID to the PID

    pid_t ppid = getppid();
     printf("ppid: %d\n", ppid); // for debugging

    char ppid_str[20];
     snprintf(ppid_str, sizeof(ppid_str), "%d", ppid); // for debugging

    setenv("PPID", ppid_str, 1);

     printf("Environment Variable: PPID = %s\n", getenv("PPID")); // for debugging

    // Step 4
    // set environment variable USER to the "ee3233"

    setenv("USER", "ee3233", 1);
    
    check_code();
    return 0;
}

void check_code()
{
    system("python3 check_env.py");

    // Add small sleep to ensure script
    // has time to run
    sleep(1);
}