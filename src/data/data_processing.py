import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class DataProcessing:

    def __init__(self, datasets):
        self.datasets = datasets  # Recevoir les chemins des fichiers téléchargés de dataLoad

    def dataprocess(self):
        # Dossier de destination pour les fichiers traités
        processed_dir = os.getenv('PROCESSED_PATH')
        os.makedirs(processed_dir, exist_ok=True)

        # Traiter chaque fichier dans le dictionnaire 'datasets'
        for name, file_path in self.datasets.items():
            try:
                # Lire chaque fichier CSV en DataFrame
                df = pd.read_csv(file_path)
                print(f"Début du traitement de {name}...")  # Message initial
                print(f"Premier aperçu des données pour {name} :")
                print(df.head())  # Afficher les 5 premières lignes du fichier

                # Suppression des doublons
                df.drop_duplicates(inplace=True)
                print(f"Doublons supprimés pour {name}.")

                # Convertir les colonnes de type date (si elles existent) en format datetime
                date_columns = [col for col in df.columns if 'timestamp' in col.lower()]
                for col in date_columns:
                    df[col] = pd.to_datetime(df[col], unit="ms")  
                print(f"Colonnes de type date converties pour {name}.")

                # Enregistrer chaque fichier traité individuellement dans 'data/processed'
                processed_file_path = os.path.join(processed_dir, f"{name}_processed.csv")
                df.to_csv(processed_file_path, index=False)
                print(f"Données traitées pour {name} enregistrées sous {processed_file_path}.")
                print(f"Aperçu des données traitées pour {name} :")
                print(df.head())  # Afficher les 5 premières lignes après traitement

            except Exception as e:
                print(f"Erreur lors du traitement de {name} : {e}")

        # Concaténer les deux fichiers 'item_properties'
        try:
            if 'item_properties_part1' in self.datasets and 'item_properties_part2' in self.datasets:
                print("Concaténation des données item_properties en cours...")
                # Charger les deux fichiers item_properties
                item_properties_part1 = pd.read_csv(self.datasets['item_properties_part1'])
                item_properties_part2 = pd.read_csv(self.datasets['item_properties_part2'])

                # Concaténer les deux DataFrames (ajouter les lignes de part2 à part1)
                combined_item_properties = pd.concat([item_properties_part1, item_properties_part2], ignore_index=True)

                # Suppression des doublons après concaténation
                combined_item_properties.drop_duplicates(inplace=True)
                combined_item_properties = pd.to_datetime(combined_item_properties, unit='ms') 
                print("Concaténation des données item_properties réussie.")

                # Enregistrer la version concaténée dans le même dossier
                combined_file_path = os.path.join(processed_dir, 'item_properties_combined_processed.csv')
                combined_item_properties.to_csv(combined_file_path, index=False)
                print(f"Concaténation des données item_properties enregistrée sous {combined_file_path}.")
                print("Aperçu des données concaténées item_properties :")
                print(combined_item_properties.head())

        except Exception as e:
            print(f"Erreur lors de la concaténation des données item_properties : {e}")

