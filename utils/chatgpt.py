from openai import OpenAI

from helper import load_config

config = load_config()
ForwardKey = config["chatgpt"]["ForwardKey"]
base_url = config["chatgpt"]["url"]
model = config["chatgpt"]["model"]


class Main:

    client = OpenAI(
        api_key=ForwardKey,
        base_url=base_url,
    )

    def chat(self, query, history):

        history += [{
            "role": "user",
            "content": query
        }]

        completion = self.client.chat.completions.create(
            model=model,
            messages=history,
        )

        result = completion.choices[0].message.content

        history += [{
            "role": "assistant",
            "content": result
        }]

        return history, result, completion.usage.total_tokens
