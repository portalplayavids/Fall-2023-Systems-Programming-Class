#define BUF_SIZE 1024

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
    Fd3 = open(argv[5], O_RDONLY); /*A*/
    Fd4 = open(argv[7], O_RDONLY); /*B*/

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