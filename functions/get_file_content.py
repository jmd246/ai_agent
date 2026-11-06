import os
from openai.types.chat import ChatCompletionToolParam

MAX_CHARS: int = 10000

get_file_content_schema : ChatCompletionToolParam = {
    "type" : "function",
    "function" : {
        "name" : "get_file_content",
        "description": "Reads the content of a specified file relative to the working directory, up to a maximum number of characters",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "file_name" : {
                    "type": "string",
                    "description" : "File name to read content from, relative to the working directory",
                },
            },
        },
    }
}

def get_file_content(working_directory: str, file_name: str) -> tuple[str, bool]:
    try:
        abs_path: str = os.path.abspath(working_directory)
        file_path: str = os.path.join(abs_path, file_name)
        validate_path = os.path.commonpath([abs_path, file_path]) == abs_path
        print(file_path)
        if not validate_path:
            raise ValueError(
                f'\tError: Cannot list "{file_path}" as it is outside the permitted working directory\n'
            )
        elif not os.path.isfile(file_path):
            raise TypeError(f'\tError: "{file_path}" is not a file')
        else:
            is_truncated: bool = False
            # read the file up to MAX_CHARS characters
            with open(file_path, mode="r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    is_truncated = True
                    content += (
                        f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    )
            return content, is_truncated
            # add a message if data gets truncated
    except Exception as e:
        return str(e), False
