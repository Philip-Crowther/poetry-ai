# this file makes compiles the poetry prompt input and makes calls to the open ai api
import os, openai
import random as r

NUMBER_OF_POEMS_CREATED = 1

with open()

def generate_prompt():
    """generates a selection of random poems as a prompt"""
    prompt = ""
    return prompt


for _ in range(NUMBER_OF_POEMS_CREATED):
    openai.api_key = os.getenv("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")
    prompt = generate_prompt()
    openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=5
    )
