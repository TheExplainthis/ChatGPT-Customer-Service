import openai


class OpenAIModel:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def chat_completion(self, messages, model_engine='gpt-3.5-turbo') -> str:
        try:
            response = openai.ChatCompletion.create(
                model=model_engine,
                messages=messages
            )
            role = response['choices'][0]['message']['role']
            content = response['choices'][0]['message']['content'].strip()
            return role, content
        except Exception as e:
            raise e

    def embedding(self, text, model_engine='text-embedding-ada-002') -> list:
        try:
            response = openai.Embedding.create(
                model=model_engine,
                input=text
            )
            return response["data"][0]["embedding"]
        except Exception as e:
            raise e