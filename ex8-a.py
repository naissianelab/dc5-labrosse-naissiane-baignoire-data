import pandas as pd

chemin_fichier_csv = 'fichier.csv'

donnees_ventes = pd.read_csv(chemin_fichier_csv)

print(donnees_ventes.head())