import sqlite3
from tabulate import tabulate  # Ajoute cette importation

print("Hello, world! Je suis prête pour le Data Engineering.")

db_path = "data/pme_ventes.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Magasins (
    id_magasin INTEGER PRIMARY KEY,
    ville TEXT,
    nombre_salaries INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Produits (
    id_ref_produit TEXT PRIMARY KEY,
    nom TEXT,
    prix REAL,
    stock INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ventes (
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    date_vente TEXT,
    id_ref_produit TEXT,
    id_magasin INTEGER,
    quantite INTEGER,
    FOREIGN KEY(id_ref_produit) REFERENCES Produits(id_ref_produit),
    FOREIGN KEY(id_magasin) REFERENCES Magasins(id_magasin)
)
''')


for table in ['Magasins', 'Produits', 'Ventes']:
    cursor.execute(f"PRAGMA table_info({table})")
    columns = cursor.fetchall()
    print(f"\nStructure de la table {table}:")
    print(tabulate(columns, headers=["cid", "name", "type", "notnull", "dflt_value", "pk"], tablefmt="github"))

    # Affiche les 5 premières lignes de chaque table
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    rows = cursor.fetchall()
    if rows:
        print(f"\nExemple de données ({table}):")
        print(tabulate(rows, headers=[col[1] for col in columns], tablefmt="github"))
    else:
        print(f"\nAucune donnée dans la table {table}.")

conn.commit()
conn.close()