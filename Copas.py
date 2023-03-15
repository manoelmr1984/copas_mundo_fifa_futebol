import pandas as pd
import matplotlib.pyplot as plt

copas = pd.read_csv('WorldCups.csv')

print(copas)
print("Campeões",copas['Winner'])
print("Conta Campeões:",copas['Winner'].nunique())
print("Gols Marcados:",copas['GoalsScored'].sum())


ano_copa = copas['Year']
gols_copa = copas['GoalsScored']
plt.scatter(ano_copa,gols_copa)
#plt.show