#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() 
{
    pid_t pid_child = fork();

    if (pid_child == -1) {
        printf("Error: Failed to create child process.");
        return 1;
    } 
    else if (pid_child == 0) {
        printf("[PID %d] Child process. Parent PID = %d.\n", (int) getpid(), (int) getppid());
    } 
    
    else {
        printf("[PID %d] Parent process. Child PID = %d.\n", (int) getpid(), (int) pid_child);
    }

    return 0;
}