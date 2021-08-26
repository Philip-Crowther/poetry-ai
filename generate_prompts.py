# generates training prompts for the open-ai fine-tuning function. goal is to generate tweet-sized bits of poems,
# then separate said poems to create training data of what we want the model to produce

MAX_PROMPT_LENGTH = 280  # based off length of tweets


def generate_prompts():
    """creates twitter-sized training data"""
    poem = ''
    prompt, completion = cut_prompt(poem)
    return


def cut_prompt(poem):
    """outputs semi-randomly sectioned poem as prompt and its ideal completion"""
    return prompt, completion

