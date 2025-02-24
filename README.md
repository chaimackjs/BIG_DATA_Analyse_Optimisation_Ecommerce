# BIG_DATA_Analyse_Optimisation_Ecommerce
# Configuration de l'Environnement et Tests

## 1. Création de l'Environnement Virtuel
```sh
python -m venv env
```

## 2. Activation de l'Environnement
```sh
env\Scripts\activate  # Sous Windows
source env/bin/activate  # Sous macOS/Linux
```

## 3. Installation des Dépendances
```sh
python -m pip install -r requirements.txt
```

## 4. Exécution des Tests

### Test des Pipelines
```sh
python -m src.main
```

### Test A/B
```sh
python -m src.scripts.test_A_B
```

