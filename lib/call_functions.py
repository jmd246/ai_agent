from functions.get_files_info import get_files_info_schema
from openai.types.chat import ChatCompletionToolParam

available_functions : list[ChatCompletionToolParam] = [
    get_files_info_schema,
]