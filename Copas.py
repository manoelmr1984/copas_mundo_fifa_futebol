import pandas as pd

copas = pd.read_csv('WorldCups.csv')

print(copas)
print("Campeões",copas['Winner'])
print("Conta Campeões:",copas['Winner'].nunique())
print("Gols Marcados:",copas['GoalsScored'].sum())
