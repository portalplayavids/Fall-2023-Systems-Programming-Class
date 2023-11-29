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
        pass
    
    def parse_ls_output(self, output):
        # "parse ls -l output"
        pass
    
    def parse_ps_output(self, output):
        # "parse ps aux output"
        pass