

from openai import OpenAI, api_key
from config import settings
import util.parser
from prompts import system_prompt
from openai.types.chat import ChatCompletionMessageParam



def main():
 
    # set up the argument parser and parse the command line arguments
    parser = util.parser.Parser(data=None)
    args = parser.setup_argparse().parse_args()
    # create a list of messages to send to the OpenAI API
    messages : list[ChatCompletionMessageParam] = [
        { 
            "role": "system",
            "content": system_prompt   
        }, 
        {
            "role": "user",
            "content": args.user_prompt
        },
    ]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.openai_api_key
    )
    # send the messages to the OpenRouter API and get the response   
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    #``
    usage = response.usage
    if usage is None:
        raise RuntimeError("No response from openrouter API")
    else:

        if args.verbose:
            # print the usage information
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {usage.prompt_tokens}" )
                print(f"Response tokens: {usage.completion_tokens}" )


        # print the usage information
        # print the models response
        print(response.choices[0].message.content)



if __name__ == "__main__":
   main()



