# Exercise: Build a Command Runner and Parser Module

**Objective:** Create a custom Python module with a class that executes system commands and parses their output.

## Requirements

1. **Module and Class Setup:**
   - Create a new Python module named `command_runner.py`.
   - Inside this module, define a class named `CommandRunner`.

2. **Implementing Command Execution:**
   - In the `CommandRunner` class, implement a method `run_command` that uses `subprocess.Popen` to execute a given command.

3. **Parsing `ls -l` Output:**
   - Implement a method `parse_ls_output` that extracts file names from the output of `ls -l`.

4. **Parsing `ps aux` Output:**
   - Implement a method `parse_ps_output` that extracts command names from the output of `ps aux`.

5. **Testing:**
   - Write a script to test the `CommandRunner` class.

## Example Outline for `command_runner.py`:

```python
import subprocess

class CommandRunner:
    def run_command(self, command):
        # Implement command execution using subprocess.Popen
        pass

    def parse_ls_output(self, output):
        # Implement parsing of ls -l output
        pass

    def parse_ps_output(self, output):
        # Implement parsing of ps aux output
        pass
```


## Learning Objectives

- Understand how to use the `subprocess` module to run system commands.
- Practice parsing and processing command-line output.
- Gain experience in writing custom modules and classes in Python.

*Hint: you can use `.split` and index the list.*
