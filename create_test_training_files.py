# file will be used to create a smaller dataset of poems to test the GPT fine-tuning features
import pandas as pd

data = pd.read_csv('kaggle_poem_dataset.csv')


poets = ['Emily Dickinson', 'Walt Whitman', 'William Wordsworth', 'Robert Frost', 'Maya Angelou', 'Sylvia Plath',
         'Gwendolyn Brooks', 'Edgar Allan Poe', 'Langston Hughes', 'James Baldwin', 'Rita Dove',
         'William Carlos Williams', 'Allen Ginsberg', 'Lucille Clifton', 'Audre Lorde']

poem_table = data.loc[data['Author'].isin(poets)]

poems = pd.DataFrame(poem_table['Content'])
prompt = [''] * poems.shape[0]
poems['prompt'] = prompt
poems.rename(columns={'Content': 'completion', 'prompt': 'prompt'}, inplace=True)
print(poems.columns)
print(poems.head())

poems.to_csv('test_poems.csv', index=False)

# INSTRUCTION TO FORMAT AND TRAIN WITH PROMPTS:
# https://beta.openai.com/docs/guides/fine-tuning
