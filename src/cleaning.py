import pandas as pd

csv = pd.read_csv('resources/dictionary-crossword.csv')
print(csv.head())

true_rows = []

for row in csv.iterrows():
    true_rows.append({
        'word': row[1]['output'].strip().split(' ')[0],
        'clue': row[1]['input'].strip().split('.')[0],
    })

df = pd.DataFrame(true_rows)
df.to_csv('resources/dictionary-crossword-cleaned.csv', index=False)