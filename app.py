import pandas as pd

df = pd.read_csv('expenses.csv')
print("--------Total Expenses--------")
print(df)
category = df.groupby('Category')['Amount'].sum()
print("--------Total by Category--------")
print(category)