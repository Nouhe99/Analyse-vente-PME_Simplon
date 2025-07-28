# Base Python 
FROM python:3.10-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installer requests pour récupérer CSV 
RUN pip install pandas requests tabulate

# Copier tous les scripts et fichiers CSV dans le conteneur
COPY import_data.py analyser.py verify_import.py /app/
COPY fichiers_csv /app/fichiers_csv




# Lancer le script principal (ici, lanalyse aprés import)
CMD ["python", "analyser.py"]
