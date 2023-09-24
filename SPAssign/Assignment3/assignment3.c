#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void check_code();

int main()
{
    // Step 1
    // set environment variable ASSIGNMENT3 to "best ever"

    // Step 2
    // write code to get your process's PID
    // NOTE: the pid is of type pid_t (int for our case)
    // example code to convert int to char[]
    // char pid_str[8] = {0};
    // sprintf(pid_str, "%d", <variable used for getpid>);

    // Step 3
    // set environment variable PPID to the PID

    // Step 4
    // set environment variable USER to the "ee3233"

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