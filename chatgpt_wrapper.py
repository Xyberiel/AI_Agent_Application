import openai

class ChatGPTWrapper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt, model="text-davinci-002", max_tokens=150, n=1, stop=None, temperature=0.5):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return response.choices[0].text.strip()
