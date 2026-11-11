import json
import logging

from openai import OpenAI
from config import settings
from lib.prompts import system_prompt
from call_functions import call_function
from openai.types.chat import (
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageFunctionToolCall,
)
from call_functions import available_functions


class Agent:
    def handle_response(self, message: ChatCompletionMessage, verbose: bool) -> bool:
        if message.tool_calls is None:
            self.messages.append({"role": "assistant", "content": message.content})
            print(message.content)
            return True

        else:
            # for now print name and args of each function
            for tool_call in message.tool_calls:
                if tool_call.type == "function":
                    function_args = json.loads(tool_call.function.arguments or "{}")
                    print(
                        f"Calling function: {tool_call.function.name}({function_args})"
                    )
                    result = call_function(tool_call, verbose)
                    self.messages.append(
                        {
                            "role": "tool",
                            "content": result["content"],
                            "tool_call_id": tool_call.id,
                        }
                    )
                    if verbose:
                        print(f"-> {result['content']}")
                    logging.info(
                        f"Calling function: {tool_call.function.name}({function_args})"
                    )
            return False

    def __init__(self, **user_args) -> None:
        self.user_prompt = user_args["user_prompt"]
        self.verbose = user_args["verbose"]
        # self.iteration = user_args["iterations"]
        print(user_args)
        # create a list of messages to send to the OpenAI API
        self.messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": self.user_prompt},
        ]

    def run(self) -> bool:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1", api_key=settings.openai_api_key
        )
        iteration = 20
        complete = False
        while iteration > 0:
            # print the user id
            # send the messages to the OpenRouter API and get the response
            response = client.chat.completions.create(
                model="openrouter/free",
                messages=self.messages,
                tools=available_functions,
            )
            # ``
            usage = response.usage
            if usage is None:
                raise RuntimeError("No response from openrouter API")
            else:
                if self.verbose:
                    # print the usage information
                    print(f"User prompt: {self.user_prompt}")
                    print(f"Prompt tokens: {usage.prompt_tokens}")
                    print(f"Response tokens: {usage.completion_tokens}")

                # print the usage information
                # print the models response
                message = response.choices[0].message
                self.messages.append(
                    {"role": "assistant", "content": message.model_dump()["tool_calls"]}
                )
                complete = self.handle_response(message, self.verbose)
                if complete:
                    break
            iteration -= 1

        # if not complete:
        #    print("The task was not completed within the given iterations.")
        if not complete:
            print("The task was not completed within the given iterations.")
        return complete
