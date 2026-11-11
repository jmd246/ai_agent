

from typing import Callable

from functions.get_files_info import get_files_info_schema
from functions.write_file import write_file_schema
from functions.run_python_file import run_python_schema
from functions.get_file_content import get_file_content_schema
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content



from openai.types.chat import ChatCompletionToolParam
import json
available_functions : list[ChatCompletionToolParam] = [
    get_files_info_schema,
    write_file_schema,
    run_python_schema,
    get_file_content_schema
]
function_map : dict[str,Callable[...,str | tuple[str,bool]]] = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
    "get_file_content": get_file_content
}

#role tool_id content is a dict 
def call_function(tool_call, verbose: bool = False) -> dict:
    # hsndle the abstract tool call and save res to a dict
    #name args id
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments or "{}")
    # hard code the dir to the calculaator directory
    args["working_directory"] = "./calculator"  
    id = tool_call.id
    if name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": id,
            "content": f"Error: Unknown function: {name}",
        }
    
    result = function_map[name](**args)
    if verbose:
        print(f" - Calling function: {name}({args})")
        return {"role": "tool", "tool_id": id, "content": f"{result}"}
        
    else:
        print(f" - Calling function: {name}")
        return {
            "role": "tool",
            "tool_call_id": id,
            "content": f"{result}",
        }