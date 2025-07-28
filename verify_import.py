import sqlite3

db_path = "/app/data/pme_ventes.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(" Magasins :")
for row in cursor.execute("SELECT * FROM magasins LIMIT 5"):
    print(row)

print("\n Produits :")
for row in cursor.execute("SELECT * FROM produits LIMIT 5"):
    print(row)

print("\n Ventes :")
for row in cursor.execute("SELECT * FROM ventes LIMIT 5"):
    print(row)

conn.close()
