When a system call like `execve()` is invoked in C, it initiates a sequence of steps to execute a new program. Here are the general execution steps for the `execve()` system call:

1. **Preparing Arguments**:
   - The calling program prepares the arguments for the `execve()` call. These arguments typically include the path to the executable file, command-line arguments for the new program, and the environment variables.

2. **Kernel Mode Transition**:
   - The program transitions from user mode to kernel mode. This transition is essential because system calls operate in kernel mode, which has higher privileges and allows direct access to system resources.

3. **Validation and Permission Checks**:
   - The kernel performs checks to validate the provided arguments and verifies that the user has permission to execute the specified file.

4. **File Lookup**:
   - The kernel looks up the file specified in the path argument. It searches for the file in the file system, ensuring it exists and is accessible.

5. **Loading the New Program**:
   - If the file is found and permissions are granted, the kernel sets up a new process to run the program. This involves creating a new process control block (PCB) with its own memory space, file descriptors, and other process-specific information.

6. **Memory Allocation and Initialization**:
   - The kernel allocates memory for the new program and loads the program's code and data into the allocated memory. It sets up the program's initial stack and heap as well.

7. **Copying Arguments and Environment**:
   - The kernel copies the command-line arguments and environment variables provided by the calling program into the new process's address space.

8. **Program Execution**:
   - The kernel sets the program counter (PC) to the entry point of the loaded program and starts executing it. The new program takes over the execution, and the original program ceases to run.

9. **Cleanup and Resource Release**:
   - After the new program has finished executing, or if there was an error during any of the previous steps, the kernel performs cleanup. This includes releasing resources associated with the original process, closing file descriptors, and deallocating memory.

10. **Return to User Mode**:
    - If the `execve()` call was successful, the new program continues execution in user mode. If there was an error, an appropriate error code is returned to the calling program.

The `execve()` system call is a fundamental mechanism for process creation and program execution in Unix-like operating systems. It replaces the current process image with a new one, allowing programs to run other programs, which is a key feature of process control and management in these systems.