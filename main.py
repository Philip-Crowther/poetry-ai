# this file generates poems with the fine-tuned model

import os, openai
import random as r

NUMBER_OF_POEMS_CREATED = 1

for _ in range(NUMBER_OF_POEMS_CREATED):
    openai.api_key = os.getenv("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")
    prompt = generate_prompt()
    openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=5
    )
