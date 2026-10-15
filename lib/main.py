

from openai import OpenAI, api_key
from config import settings
import util.parser
from openai.types.chat import ChatCompletionMessageParam

def main():
 
    parser = util.parser.Parser(data=None)
    args = parser.setup_argparse().parse_args()
    messages : list[ChatCompletionMessageParam] = [{
            "role": "user",
            "content": args.user_prompt
        },
    ]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.openai_api_key
    )
       
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    usage = response.usage
    if usage is None:
        raise RuntimeError("No response from openrouter API")
    else:
        # print the usage information
        print(f"Prompt tokens: {usage.prompt_tokens}" )
        print(f"Response tokens: {usage.completion_tokens}" )
        # print the models response
        print(response.choices[0].message.content)



if __name__ == "__main__":
   main()



