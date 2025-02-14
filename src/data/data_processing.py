import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class dataProcessing:

    def __init__(self, datasets):
        self.datasets = datasets  # Recevoir les chemins des fichiers téléchargés de dataLoad

    def dataprocess(self):
        # Dossier de destination pour les fichiers traités
        processed_dir = os.getenv('PROCESSED_PATH')
        os.makedirs(processed_dir, exist_ok=True)

        for name, file_path in self.datasets.items():
            try:
                  # Lire chaque fichier CSV en DataFrame
                df = pd.read_csv(file_path)
                print(f"Processing data from {name}...")
                print(df.head()) 

                # Suppression des doublons
                df.drop_duplicates(inplace=True)
                print(f"Removed duplicates from {name}.")

                # Convertir les colonnes de type date (si elles existent) en format datetime
                # Supposons que les colonnes de type date aient des noms comme 'date', 'timestamp', etc.
                date_columns = [col for col in df.columns if   'timestamp' in col.lower()]
                for col in date_columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')  # 'coerce' met NaT pour les valeurs non convertibles
                print(f"Converted date columns in {name}.")

                # Enregistrer le fichier nettoyé dans le dossier 'data/processed'
                processed_file_path = os.path.join(processed_dir, f"{name}_processed.csv")
                df.to_csv(processed_file_path, index=False)
                print(f"Processed data saved to {processed_file_path}")

                # Afficher les premières lignes du fichier traité
                print(f"Preview of cleaned data from {name}:")
                print(df.head())  # Afficher les 5 premières lignes du fichier nettoyé


            except Exception as e:
                print(f"Error processing {name}: {e}")
