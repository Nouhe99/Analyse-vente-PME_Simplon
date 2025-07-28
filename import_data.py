# -*- coding: utf-8 -*-

import sqlite3
import csv
import os

db_path = "/app/data/pme_ventes.db"
csv_folder = "/app/fichiers_csv"

# Connexion à la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Import magasins
with open(os.path.join(csv_folder, "Donnees brief data engineer - magasins.csv"), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT OR IGNORE INTO Magasins (id_magasin, ville, nombre_salaries)
            VALUES (?, ?, ?)
        ''', (row['ID Magasin'], row['Ville'], row['Nombre de salaries']))

# Import produits
with open(os.path.join(csv_folder, "Donnees brief data engineer - produits.csv"), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT OR IGNORE INTO Produits (id_ref_produit, nom, prix, stock)
            VALUES (?, ?, ?, ?)
        ''', (row['ID Référence produit'], row['Nom'], row['Prix'], row['Stock']))

# Import ventes
with open(os.path.join(csv_folder, "Donnees brief data engineer - ventes.csv"), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT INTO Ventes (date_vente, id_ref_produit, id_magasin, quantite)
            VALUES (?, ?, ?, ?)
        ''', (row['Date'], row['ID Référence produit'], row['ID Magasin'], row['Quantité']))

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print(" Données insérées manuellement avec succés dans la base.")
