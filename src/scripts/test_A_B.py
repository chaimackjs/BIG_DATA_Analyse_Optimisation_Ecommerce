import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os
import scipy.stats as stats

load_dotenv()

class ab_test():
    def __init__(self):
        self.processed_path = os.getenv('PROCESSED_PATH')

    def repartition(self):

        # Simulation des données pour les utilisateurs
        np.random.seed(42)  # Pour garantir la reproductibilité

        # Nombre d'utilisateurs dans chaque groupe
        n_blue_button = 10000  # Groupe avec bouton bleu
        n_red_button = 10000   # Groupe avec bouton rouge

        # Taux de conversion simulé pour chaque groupe
        conversion_rate_blue_button = 0.2796  # 27.96% de conversion pour le bouton bleu
        conversion_rate_red_button = 0.2850   # 28.50% de conversion pour le bouton rouge

        # Simulation des conversions en fonction des groupes
        blue_button_conversions = np.random.binomial(n_blue_button, conversion_rate_blue_button)
        red_button_conversions = np.random.binomial(n_red_button, conversion_rate_red_button)

        # Calcul des taux de conversion pour chaque groupe
        conversion_rate_blue_button_simulated = blue_button_conversions / n_blue_button
        conversion_rate_red_button_simulated = red_button_conversions / n_red_button

        # Affichage des résultats des taux de conversion
        print(f'Taux de conversion pour le bouton bleu : {conversion_rate_blue_button_simulated:.4f}')
        print(f'Taux de conversion pour le bouton rouge : {conversion_rate_red_button_simulated:.4f}')

        # Test A/B : Test de différence de proportions (test Z)
        # H0 : les taux de conversion des deux groupes sont égaux
        # H1 : les taux de conversion des deux groupes sont différents
        p1 = conversion_rate_blue_button_simulated
        p2 = conversion_rate_red_button_simulated
        n1 = n_blue_button
        n2 = n_red_button

        # Calcul de la variance combinée
        pooled_p = (blue_button_conversions + red_button_conversions) / (n1 + n2)
        std_error = np.sqrt(pooled_p * (1 - pooled_p) * (1/n1 + 1/n2))

        # Calcul de la statistique z
        z = (p1 - p2) / std_error

        # Calcul de la p-value pour le test bilatéral
        p_value = 2 * (1 - stats.norm.cdf(abs(z)))

        # Résultats du test
        print(f'Statistique Z : {z:.4f}')
        print(f'P-value : {p_value:.4f}')

        # Interprétation
        if p_value < 0.05:
            print("La différence entre les groupes est statistiquement significative. Il est probable que la couleur du bouton influence le taux de conversion.")
        else:
            print("La différence entre les groupes n'est pas statistiquement significative.")


test = ab_test()

test.repartition()