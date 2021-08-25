# generates training prompts for the open-ai fine-tuning function. goal is to generate tweet-sized bits of poems,
# then separate said poems to create training data of what we want the model to produce

POEMS = open('poem_pieces.txt', 'r', encoding='utf-8').read().split('\n\n')
PROMPT_LENGTH = 3000


def generate_prompt():
    """generates a selection of random poems as a prompt"""
    api_prompt = ""
    while len(api_prompt) < PROMPT_LENGTH-500:
        api_prompt += r.choice(POEMS)
        api_prompt += '\n'
    return api_prompt
