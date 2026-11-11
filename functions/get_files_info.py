import os

from openai.types.chat import ChatCompletionToolParam

# scchem for this function is is a json format as its what open ai expects
get_files_info_schema: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    # validate that the path to the directory is inside the working_directory.
    output: str = str()
    try:
        abs_path: str = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        validate_path = os.path.commonpath([abs_path, target_dir]) == abs_path
        if directory == ".":
            output += f"Results for current working directory: \n"
        else:
            output += f"Results for {directory} directory: \n"
        if not validate_path:
            raise ValueError(
                f'\tError: Cannot list "{directory}" as it is outside the permitted working directory\n'
            )
        elif not os.path.isdir(target_dir):
            raise TypeError(f'\tError: "{directory}" is not a directory')
        else:
            # success_message = f"Success: {directory} is within the working directory"
            # iterate over the files in the directory and get their information
            file_info: str = ""
            for item in os.listdir(target_dir):
                item_path = os.path.join(target_dir, item)
                file_info += f"{read_file_info(item_path, item)}"
            return output + file_info
    except Exception as e:
        return output + str(e)


def read_file_info(file_path: str, file_name: str) -> str:
    file_size: int = os.path.getsize(file_path)
    is_dir: bool = os.path.isdir(file_path)
    return f"   - {file_name}: file_size={file_size}, is_dir={is_dir}\n"
