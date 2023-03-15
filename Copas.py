import streamlit as st
import pandas as pd

print("Manoel")
#copas = pd.read_csv('WorldCups.csv')
copas=pd.read_csv('https://github.com/manoelmr1984/copas_mundo_fifa_futebol/blob/main/WorldCups.csv')

print(copas)
print("Campeões",copas['Winner'])
print("Conta Campeões:",copas['Winner'].nunique())
print("Gols Marcados:",copas['GoalsScored'].sum())
