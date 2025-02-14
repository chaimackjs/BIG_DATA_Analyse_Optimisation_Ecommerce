# Importation des classes
from .data import dataLoad, dataProcessing

def main():
    # Créer une instance de la classe dataLoad
    dataLoad_test = dataLoad()

    # Charger les données via la méthode load_data()
    datasets = dataLoad_test.load_data()

    # Créer une instance de dataProcessing avec les datasets chargés
    dataLoad_test2 = dataProcessing(datasets)

    # Appeler la méthode de traitement des données
    dataLoad_test2.dataprocess()

    # Afficher les datasets pour vérification
    print(f"Datasets: {dataLoad_test.datasets}")

if __name__ == "__main__":
    main()
