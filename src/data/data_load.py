from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class DataLoad:

    def __init__(self, datasets=None):
        self.RAW_PATH = os.getenv('RAW_PATH')
        self.KAGGLE_DATASET = os.getenv('KAGGLE_DATASET')
        self.datasets = datasets or {
            "category_tree" : "category_tree.csv",
            "events" : "events.csv",
            "item_properties_part1" : "item_properties_part1.csv",
            "item_properties_part2" : "item_properties_part2.csv",
            

        }
        self.api = KaggleApi()
        self.api.authenticate()

    def download_data(self):
        self.api.dataset_download_files(dataset=self.KAGGLE_DATASET, path=self.RAW_PATH, unzip=True)    
        print(f"Data downloaded to {self.RAW_PATH}")

    def load_data(self):
        datasets={}
        for name, file in self.datasets.items():
            file_path = os.path.join(self.RAW_PATH, file)
            if not os.path.exists(file_path):
                print(f"File {file} not found at {file_path}")
                self.download_data()   
            datasets[name] = file_path
        print(f"Data loaded: {datasets}")
        return datasets         



