
from openai import OpenAI, api_key
from config import settings

def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.openai_api_key
    )
       
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
            }
        ]
    )

    # print the models response

    print(response.choices[0].message.content)



if __name__ == "__main__":
    main()
