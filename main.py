from openai import OpenAI, api_key
from config import settings
from lib.util.parser import Parser
from lib.prompts import system_prompt
from lib.call_functions import call_function
from openai.types.chat import ChatCompletionMessage, ChatCompletionMessageParam, ChatCompletionMessageFunctionToolCall
from lib.call_functions import available_functions
import json
import logging


logging.basicConfig(level=logging.INFO,filename="openrouter.log", filemode="w")

def handle_response(message: ChatCompletionMessage,verbose : bool) -> None :
    if message.tool_calls is None:
        print(message.content)
    else:
        # for now print name and args of each function
       for tool_call in message.tool_calls:
            if tool_call.type == "function":
                function_args = json.loads(
                    tool_call.function.arguments or "{}"
                )
                print(f"Calling function: {tool_call.function.name}({function_args})")
                result = call_function(tool_call, verbose)
                if verbose:
                    print(f"-> {result['content']}")
                logging.info(f"Calling function: {tool_call.function.name}({function_args})")

    # check response for what function to call perofrm the call and return the results back to the llm

def main():
    # set up the argument parser and parse the command line arguments
    
    parser = Parser(data=None)
    args = parser.setup_argparse().parse_args()
    # create a list of messages to send to the OpenAI API
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=settings.openai_api_key
    )
    print(f"portion of key used is {settings.openai_api_key[-4:]}")
    # print the user id
    # send the messages to the OpenRouter API and get the response
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools = available_functions,
    )
    # ``
    usage = response.usage
    if usage is None:
        raise RuntimeError("No response from openrouter API")
    else:
        if args.verbose:
            # print the usage information
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Response tokens: {usage.completion_tokens}")

        # print the usage information
        # print the models response
        handle_response(response.choices[0].message, args.verbose)


if __name__ == "__main__":
    main()
