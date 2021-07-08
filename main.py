# this file makes compiles the poetry prompt input and makes calls to the open ai api
import os, openai
import random as r

NUMBER_OF_POEMS_CREATED = 1
POEMS = open('poem_pieces.txt', 'r', encoding='utf-8').read().split('\n\n')
PROMPT_LENGTH = 3000


def generate_prompt():
    """generates a selection of random poems as a prompt"""
    api_prompt = ""
    while len(api_prompt) < PROMPT_LENGTH-500:
        api_prompt += r.choice(POEMS)
        api_prompt += '\n'
    return api_prompt


for _ in range(NUMBER_OF_POEMS_CREATED):
    openai.api_key = os.getenv("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")
    prompt = generate_prompt()
    openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=5
    )
