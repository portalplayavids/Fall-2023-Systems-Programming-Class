# Description:
#
# Custom Python Module with a class that executes
# System commands and parses their output.
#######################################################
# Requirements:
#
# 1. Module and Class setup:
#   a. Create a module called command_runner.py
#   b. Create a class called CommandRunner
#######################################################
# 2. Implementing Command Execution:
#   a. In the CommandRunner class, implement a
#      run_command method using 'subprocess.Popen'
#      to execute a command.
#######################################################
# 3. Parsing 'ls -l' Output:
#   a. Implement a parse_ls_output method that extracts
#      the file names from the output of 'ls -l'
#######################################################
# 4. Parsing 'ps aux' Output:
#   a. Implement a parse_ps_output method that extracts
#      commands names from the output of 'ps aux'
#######################################################
# 5. Testing:
#   a. Seperately, create a script to test CommandRunner
#######################################################

import subprocess

class CommandRunner:
    def run_command(self, command):
        # "command execution via popen"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
        # Handle errors if needed
            print(f"Error executing command: {stderr.decode().strip()}")
        return None

    def parse_ls_output(self, output):
        # "parse ls -l output"
        lines = output.strip().split('\n')
        files = []
        for line in lines[1:]: # Skip the first line which is the total
            parts = line.split()

            if len(parts) > 8:
                files.append(parts[8]) # File name is typically the 9th element
        return files


    def parse_ps_output(self, output):
        # "parse ps aux output"
        processes = []
        lines = output.strip().split('\n')
        for line in lines[1:]: # Skip the header line
            parts = line.split()
            if len(parts) > 10:
                command = ' '.join(parts[10:]) # Command is the remaining parts after 10th element
                processes.append(command)
        return processes
