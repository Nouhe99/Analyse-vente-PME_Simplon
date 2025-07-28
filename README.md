#  Projet Data Engineer - Analyse des Ventes d'une PME

Ce projet a été réalisé dans le cadre de la journée de sélection pour le parcours Data Engineer chez **Simplon.co**.

---

##  Objectif

Analyser les ventes d’une PME à partir de trois fichiers CSV (`ventes.csv`, `produits.csv`, `magasins.csv`) en utilisant :

- une base de données **SQLite**
- des scripts Python
- une architecture **Docker** orchestrée avec **Docker Compose**

---


##  Architecture Docker

Le projet utilise **deux services** via Docker Compose :

- `script-runner` : Service qui exécute les scripts Python
- `sqlite` : Service contenant l’environnement avec la CLI SQLite

###  Volumes partagés

- `./data` : pour stocker et accéder à la base SQLite
- `./fichiers_csv` : pour accéder aux fichiers CSV depuis le conteneur

---

##  Installation & Lancement

```bash
1. Cloner le projet
git clone https://github.com/Nouhe99/Nouhe99-Analyse-vente-PME_Simplon.git
cd Simplon_Test_DATA

2. Construire et exécuter avec Docker Compose
bash
Copier
Modifier
docker-compose up --build
⚠️ Le script principal analyser.py sera exécuté automatiquement.

3. Exécuter un script manuellement
bash
Copier
Modifier
docker-compose run --rm script-runner python import_data.py
docker-compose run --rm script-runner python verify_import.py

 Analyses réalisées
Le fichier analyser.py permet d'obtenir :

Le total des ventes par produit

Le chiffre d'affaires par magasin

Le nombre de ventes par date



🛠️ Dépendances
Python 3.10

pandas

requests (optionnel)

SQLite3

Docker & Docker Compose

👩‍💻Projet par : Nouha Chebbi
Candidate pour la formation Data Engineer — Simplon.co

📬 Contact
Pour toute question ou retour : chebbi.nouhe@gmail.com
