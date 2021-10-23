# creates dataset of poems to fine-tune poetry model
import pandas as pd

data = pd.read_csv('kaggle_poem_dataset.csv')

author_frequency = data['Author'].value_counts()
# TODO: create training set of said poems

poem_table = data.loc[data['Author'].isin(poets)]

poems = pd.DataFrame(poem_table['Content'])
prompt = [''] * poems.shape[0]
poems['prompt'] = prompt
poems.rename(columns={'Content': 'completion', 'prompt': 'prompt'}, inplace=True)
print(poems.columns)
print(poems.head())

poems.to_csv('test_poems.csv', index=False)
