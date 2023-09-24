//Elijah Guzman - nze594

// Run `gcc main.c -o main` to compile.
//
// Usage:
//     ./main <src> <dst1> <dst2>

#pragma once
#ifndef _FILE_COPY_MAIN
#define _FILE_COPY_MAIN

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Copies the contents of the file specified by src to the file specified by dst.
 *
 * @param src The path to the source file.
 * @param dst The path to the destination file.
 */
void copy_file(char* src, char* dst) {
    // Declare two pointers for the file handles (one for input, one for output)
    FILE* srcFile;
    FILE* dstFile;

    // Initialize the source file handle by opening a handle to the specified file.
    srcFile = fopen(src, "r+");
    if (srcFile == NULL) {
        printf("Error opening src file %s\n", src);
        exit(1);
    }

    // Initialize the destination file handle by opening a handle to the specified file.
    dstFile = fopen(dst, "w");
    if (dstFile == NULL) {
        printf("Error opening dst file %s\n", dst);
        exit(1);
    }

    // Read the input from the source file handle and write it to the
    // destination file handle.
    char c;
    while ((c = fgetc(srcFile)) != EOF) {
        fputc(c, dstFile);
    }

    // Close the file handles.
    fclose(dstFile);
    fclose(srcFile);
}

int main(int argc, char* argv[]) {
    // Read the command line arguments for the source file, and the two destination files.
    char* src = argv[1];
    char* dst1 = argv[2];
    char* dst2 = argv[3];

    // Copy the contents of the source file to the two destination files.
    copy_file(src, dst1);
    copy_file(src, dst2);
}

#endif