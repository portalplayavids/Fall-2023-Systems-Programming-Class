// Elijah Guzman - nze594 - 09/25/2023
// Description: copies text from 'source1.txt' to 'destination1.txt' and 'source2.txt' to 'destination2.txt'
// Usage: myCopy source1.txt destination1.txt source2.txt destination2.txt
#define BUF_SIZE 1024

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    int Fd1, Fd2, Fd3, Fd4, openFlags;
    mode_t filePerms;
    ssize_t num;
    char buf[BUF_SIZE];

    openFlags = O_CREAT | O_WRONLY | O_TRUNC;
    filePerms = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH;

    //Use the arguments of the functions from the given program above:
    // fd = open(pathname, flags, mode);
    // numread = read(fd, buf, count);
    // numwritten = write(fd, buf, count);
    
    Fd1 = open(argv[1], O_RDONLY);
    Fd2 = open(argv[3], O_RDONLY);
    Fd3 = open(argv[5], openFlags, filePerms);
    Fd4 = open(argv[7], openFlags, filePerms);

    while ((num = read(Fd1, buf, BUF_SIZE)/*C*/) > 0) {
        if(write(Fd2, buf, num)/*D*/ != num) {
            fatal("This is a fatal error");
        }
    }
    while ((num = read(Fd3, buf, BUF_SIZE)/*E*/) > 0) {
        if(write(Fd4, buf, num)/*F*/ != num) {
            fatal("This is a fatal error");
        }
    }
    exit(EXIT_SUCCESS);
}