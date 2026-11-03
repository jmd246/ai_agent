import os


def write_file(working_dir: str, f_path: str, content: str) -> str:
    # if path is outisde working directory return err string
    abs_path = os.path.abspath(os.path.join(working_dir, f_path))
    try:
        if not abs_path.startswith(os.path.abspath(working_dir)):
            return f'Error: Cannot write to "{f_path}" as it is outside the permitted working directory'
        elif os.path.isdir(abs_path):
            f'Error: Cannot write to "{f_path}" as it is a directory'
        else:
            # ensure directory exists
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, mode="w") as f:
                f.write(content)
            return (
                f'Successfully wrote to "{f_path}" ({len(content)} characters written)'
            )
    except Exception as e:
        return f"Error: {str(e)}"
