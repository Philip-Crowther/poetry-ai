# file will be used to create a smaller dataset of poems to test the GPT fine-tuning features
import pandas as pd

data = pd.read_csv('kaggle_poem_dataset.csv')


poets = ['Emily Dickinson', 'Walt Whitman', 'William Wordsworth', 'Robert Frost', 'Maya Angelou', 'Sylvia Plath',
         'Gwendolyn Brooks', 'Edgar Allan Poe', 'Langston Hughes', 'James Baldwin', 'Rita Dove',
         'William Carlos Williams', 'Allen Ginsberg', 'Lucille Clifton', 'Audre Lorde']

poems = data.loc[data['Author'].isin(poets)]
