
import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    #validate that the path to the directory is inside the working_directory.
    try:
        abs_path : str = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        validate_path = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not validate_path:
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        elif not os.path.isdir(target_dir):
            raise TypeError(f'Error: "{directory}" is not a directory')
        else :
            return f"Success: {directory} is within the working directory"
    except Exception as e:
        return "Error: " + str(e)