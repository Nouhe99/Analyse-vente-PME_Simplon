# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
from tabulate import tabulate

db_path = "/app/data/pme_ventes.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connexion à la base...")

# Table Analyses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_analyse TEXT,
        total_ca REAL
    )
""")

# Chiffre d'affaires total
cursor.execute("""
    SELECT SUM(v.quantite * p.prix)
    FROM Ventes v JOIN Produits p ON v.id_ref_produit = p.id_ref_produit
""")
total_ca = cursor.fetchone()[0]
print("\nChiffre d'affaires total :", total_ca, "euros")

# Enregistrer l’analyse
date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO Analyses (date_analyse, total_ca) VALUES (?, ?)", (date_now, total_ca))
conn.commit()

# Ventes par produit
cursor.execute("""
    SELECT p.nom, SUM(v.quantite) as total_ventes
    FROM Ventes v
    JOIN Produits p ON v.id_ref_produit = p.id_ref_produit
    GROUP BY p.nom
""")
produits_data = cursor.fetchall()
print("\nVentes par produit :")
print(tabulate(produits_data, headers=["Produit", "Total ventes"], tablefmt="grid"))

# Ventes par région
cursor.execute("""
    SELECT m.ville, SUM(v.quantite * p.prix) as chiffre_affaires
    FROM Ventes v
    JOIN Produits p ON v.id_ref_produit = p.id_ref_produit
    JOIN Magasins m ON v.id_magasin = m.id_magasin
    GROUP BY m.ville
""")
regions_data = cursor.fetchall()
print("\nVentes par région :")
print(tabulate(regions_data, headers=["Ville", "Chiffre d'affaires (€)"], tablefmt="grid"))

conn.close()
print("\nAnalyse terminée.")
