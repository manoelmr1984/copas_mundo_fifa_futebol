import streamlit as st
import pandas as pd

print("Manoel")
copas = pd.read_csv('WorldCups.csv')

print(copas)
print("Campeões",copas['Winner'])
print("Conta Campeões:",copas['Winner'].nunique())
print("Gols Marcados:",copas['GoalsScored'].sum())
