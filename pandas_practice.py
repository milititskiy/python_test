import pandas as pd

df = pd.read_csv('names.csv')

emails = df[(df['email'])]

print(emails)
