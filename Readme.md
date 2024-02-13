# Système de Recherche Documentaire

Ce projet implémente un système de recherche documentaire avancé permettant de filtrer et de classer des documents basés sur une requête utilisateur. Il utilise des techniques de traitement du langage naturel pour améliorer la pertinence des résultats.

## Fonctionnalités

- **Lecture et Traitement de la Requête :** Le système lit une requête utilisateur, la tokenise, et applique un prétraitement similaire à celui des documents indexés.
- **Filtrage des Documents :** Les documents peuvent être filtrés selon qu'ils contiennent tous les tokens de la requête (filtre ET) ou au moins un token (filtre OU), selon le choix de l'utilisateur.
- **Ranking des Documents :** Implémentation du score BM25 pour le classement des documents selon leur pertinence par rapport à la requête.
- **Gestion des Stop Words :** Les tokens significatifs reçoivent un poids plus important dans le calcul du score de pertinence par rapport aux stop words.
- **Exportation des Résultats :** Les résultats sont exportés dans un fichier `results.json`, incluant le titre et l'URL de chaque document pertinent.

## Les modules

Chaque module de ce projet joue un rôle clé dans le fonctionnement du système de recherche documentaire. `crawler_data_reader.py` lit et charge les données issues du crawling, essentielles pour construire l'index et pour le traitement des requêtes. `file_writer.py` gère l'écriture des résultats de la recherche dans un fichier JSON, permettant une sortie structurée et facilement accessible. `filtering.py` applique le filtrage des documents basé sur la présence de tokens, en supportant les logiques ET/OU selon la préférence de l'utilisateur. `main.py` sert de point d'entrée pour exécuter le système, gérant la saisie de la requête, le choix du filtrage, et l'affichage des résultats. `preprocessing.py` prétraite les requêtes et les documents pour améliorer la pertinence de la recherche, notamment par la tokenisation et le nettoyage des données. `ranking.py` évalue et classe les documents filtrés selon leur pertinence par rapport à la requête, en utilisant des métriques avancées comme le score BM25.

## Utilisation

Pour utiliser le système, exécutez `main.py` et suivez les instructions à l'écran pour entrer votre requête et choisir le type de filtrage (ET/OU).

```bash
python main.py
```


## Dépendances

Le projet utilise NLTK pour le traitement du langage naturel. Assurez-vous d'avoir installé NLTK avant de lancer le système :

```bash
pip install nltk
```