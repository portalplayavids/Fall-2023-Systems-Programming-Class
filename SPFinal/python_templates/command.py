import subprocess


class Command:
    @staticmethod
    def run_command(cmd: str) -> str:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode()
