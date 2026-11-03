import os
import subprocess
from sys import stderr


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        if not abs_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        # check if its a regular file if not return a err string
        elif not os.path.isfile(abs_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        # check if its a python file if not return a err string
        elif not abs_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        # we want a subprocess to run the file so for now we create a list strings
        else:
            command = ["python", abs_path]
            # if any extra ags have been passed add them to the list
            if args is not None:
                command.extend(args)
            # run the file
            completed_process = subprocess.run(
                command, stdout=subprocess.PIPE, stderr=stderr, text=True, timeout=30
            )

            if completed_process.returncode == 0:
                return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
            else:
                output = f"Process exited with code {completed_process.returncode}\n"
                if not completed_process.stdout and not completed_process.stderr:
                    output += "No output produced"
                if completed_process.stdout:
                    output += f"STDOUT: {completed_process.stdout}\n"

                if completed_process.stderr:
                    output += f"STDERR:{completed_process.stderr}\n"

                return f"Error: executing Python file: {completed_process.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
