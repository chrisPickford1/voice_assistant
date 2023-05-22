import openai
from ._base import IGPTResponseGenerator


class GPTResponseGenerator(IGPTResponseGenerator):
    def __init__(self):
        pass

    def submit(self, query: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            propmpt=query,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response["choices"][0]["text"]
