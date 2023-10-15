#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

// Function to print file details
void printDetails(const char* file) {
    struct stat fileStat;
    if (stat(file, &fileStat) == 0) {
        // Print file name
        printf("File: %s\n", file);

        // Print file permissions
        printf("Permissions: ");
        printf((fileStat.st_mode & S_IRUSR) ? "r" : "-");
        printf((fileStat.st_mode & S_IWUSR) ? "w" : "-");
        printf((fileStat.st_mode & S_IXUSR) ? "x" : "-");
        printf(" ");
        printf((fileStat.st_mode & S_IRGRP) ? "r" : "-");
        printf((fileStat.st_mode & S_IWGRP) ? "w" : "-");
        printf((fileStat.st_mode & S_IXGRP) ? "x" : "-");
        printf(" ");
        printf((fileStat.st_mode & S_IROTH) ? "r" : "-");
        printf((fileStat.st_mode & S_IWOTH) ? "w" : "-");
        printf((fileStat.st_mode & S_IXOTH) ? "x" : "-");
        printf("\n");

        // Print file owner and group
        printf("Owner: %d\n", fileStat.st_uid);
        printf("Group: %d\n\n", fileStat.st_gid);
    }
}

// Function to list details of files with a given extension in a directory
void details(const char* ext, const char* directory) {
    struct dirent* entry;
    DIR* dir = opendir(directory);

    if (dir) {
        while ((entry = readdir(dir)) != NULL) {
            if (entry->d_type == DT_REG && strstr(entry->d_name, ext) != NULL) {
                char file_path[256];
                snprintf(file_path, sizeof(file_path), "%s/%s", directory, entry->d_name);
                printDetails(file_path);
            }
        }
        closedir(dir);
    }
}

// Function to search for a keyword in the filenames of files with a given extension in a directory
void search(const char* ext, const char* directory, const char* search_keyword) {
    struct dirent* entry;
    DIR* dir = opendir(directory);

    if (dir) {
        while ((entry = readdir(dir)) != NULL) {
            if (entry->d_type == DT_REG && strstr(entry->d_name, ext) != NULL) {
                if (strstr(entry->d_name, search_keyword) != NULL) {
                    char file_path[256];
                    snprintf(file_path, sizeof(file_path), "%s/%s", directory, entry->d_name);
                    printf("Keyword \"%s\" found in: %s\n", search_keyword, file_path);
                }
            }
        }
        closedir(dir);
    }
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        printf("Usage: ./Assignment_4 <operation> <ext> <directory> [<search_keyword>]\n");
        return 1;
    }

    const char* operation = argv[1];
    const char* ext = argv[2];
    const char* directory = argv[3];

    if (strcmp(operation, "details") == 0) {
        if (argc != 4) {
            printf("Usage: ./Assignment_4 details <ext> <directory>\n");
            return 1;
        }
        details(ext, directory);
    } else if (strcmp(operation, "search") == 0) {
        if (argc != 5) {
            printf("Usage: ./Assignment_4 search <ext> <directory> <search_keyword>\n");
            return 1;
        }
        const char* search_keyword = argv[4];
        search(ext, directory, search_keyword);
    } else {
        printf("Usage: ./Assignment_4 <operation> <ext> <directory> [<search_keyword>]\n");
        return 1;
    }

    return 0;
}
