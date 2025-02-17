# Importation des classes
from .data import DataLoad

from .data import DataProcessing

from .data import DataAnalysis


def main():
    # Créer une instance de la classe dataLoad
    dataLoad_test = DataLoad()

    # Charger les données via la méthode load_data()
    datasets = dataLoad_test.load_data()

    # Créer une instance de dataProcessing avec les datasets chargés
    dataLoad_test2 = DataProcessing(datasets)

    # Appeler la méthode de traitement des données
    dataLoad_test2.dataprocess()

    #appeler les methodes d analyses
   
   
    analyse = DataAnalysis()

    analyse.run_all_analyses()


    # Afficher les datasets pour vérification
    print(f"Datasets: {dataLoad_test.datasets}")

if __name__ == "__main__":
    main()
