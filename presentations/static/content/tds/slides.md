# Plan

- Présentation générale
- Collection
- Visualisation
- Stockage
- Prédiction
- Proposition de trajet
- Bonnes pratiques

---

## OpenBikes c'est quoi ?

- **Visualiser** les vélibs en (quasi) temps réel
- Faire de la **prédiction** pour optimiser les trajets (gratuitement)
- **Conseiller** les villes pour **acheminer** les vélos entre stations (depuis le concours)

---

<div class="stretch">
  <iframe src="http://openbikes.co/en/index" height="100%" width="100%" />
</div>

---

## Carte de Toulouse un dimanche matin

![Toulouse](/static/content/tds/toulouse.png)

---

## Selection de trajet

![Formulaire](/static/content/tds/formulaire.png)

---

## Affichage du trajet optimal

![Trajet](/static/content/tds/trajet.png)

---

## L'équipe

- Max Halford
- Axel Bellec
- Notre premier site web (et pas le dernier!)

---

## Sous le capot

- Un robot codé en **Python** qui collectionne les données toutes les minutes
- Visualisation avec **Flask** et **LeafletJS**
- Stockage des données avec **MongoDB**
- Prédiction avec **sklearn**
- Un ensemble de règles et un stack basé sur l'**API Google Maps** pour établir des trajets
- Redistribution des données via une **API**
- La sauce secrète

---

## Flowchart

![Flowchart](/static/content/tds/flowchart.jpg)

---

# Collection des données

---

## Les données, concrètement

- Le nombre de vélos + le moment de la mise à jour pour chaque station
- Autant de villes que de formats de données (presque)
- Besoin d'**uniformiser les données** le plut tôt possible pour **généraliser les traitements** par la suite

---

## Ce qu'il ne faut pas faire

![DSSG1](/static/content/tds/dssg.png)
![DSSG2](/static/content/tds/dssg2.png)

---

## Normalisation

![Normalisation](/static/content/tds/normalisation.png)

---

## Code pour JCDecaux (1)

```python
import requests
import json

def stations(city):
    url = 'https://api.jcdecaux.com/vls/v1/'
    data = requests.get(url, apiKey=keys.jcdecaux, contract=city)
    stations = data.json()
    return normalize(stations)
```

---

## Code pour JCDecaux (2)

```python
from datetime import datetime

def normalize(stations):
    normalized = lambda station: {
        'name': station['name'],
        'address': station['address'],
        'lat': station['position']['lat'],
        'lon': station['position']['lng'],
        'status': station['status'],
        'bikes': station['available_bikes'],
        'stands': station['available_bike_stands'],
        'update': datetime.fromtimestamp(station['last_update']).isoformat()
    }
    return [normalized(station) for station in stations]
```

---

## Automatisation

- On définit une fonction de **récupération** et de **normalisation** par fournisseur de données
- Une file d'attente parallèle (RabbitMQ) gère les appels aux fonctions à un **intervalle régulier** (1 minute suffit)
- Les données sont stockées au fur et à mesure (boucle infinie)

---

# Affichage

---

## LeafletJS

- Permet d'afficher des points, des lignes et des polygones
- Grande communauté, beaucoup de plugins, très maintenu
- Compatible avec tous les formats de données populaires

---

## Flask

- Framework Python pour développer un site web
- Très "Pythonesque", extrêmement modulable
- Simple, rapide, documenté...

---

## Pour chaque ville, toutes les minutes, on...

- récupère les données pour la ville,
- les sauvegarde en fichier geoJSON,
- garde seulement les données les plus récentes.

---

## Quand un utiliser accède à une URL, LeafletJS...

- ouvre le fichier geoJSON de la ville,
- centre la carte sur la ville,
- parcourt chaque station et l'affiche sur la carte.

---

## Avantages de Flask + LeafletJS

- Un seul fichier pour toutes les cartes.
- Rapide à apprendre, développement rapide.
- Les deux sont très utilisés donc beaucoup de posts sur StackOverflow :)

---

# Stockage des données

---

## Que nous faut-il ?

- Date et heure
- Nombre de vélos
- Nombre de places
- La position géographique
- La météo

---

# Pourquoi MongoDB ?

- Pas besoin d'un schéma compliqué
- Extrêmement simple à mettre en place
- Très fort en écriture (WiredTiger)
- Pour s'entraîner/changer...

---

# Avant

![Avant](/static/content/tds/avant.png)

---

# Après

![Après](/static/content/tds/apres.png)

---

# Prédiction

---

## Objectifs

- Aider un utilisateur à choisir une station
- Aider les villes à acheminer les vélos d'une station à une autre

---

## Exemple de données

![Donnees](/static/content/tds/donnees.png)
<<<<<<< HEAD

---

## Allure des courbes

![Courbes](/static/content/tds/courbes.png)

---

## Carte de chaleur

![Heatmap](/static/content/tds/heatmap.png)

---

## Apprentissage supervisé

- Prédire une valeur en fonction d'une observation
- S'entraîner sur des données réelles (*train*)
- Evaluation d'une méthode via une validation croisée (*test*)

---

## Dilemne biais-variance

![bias-variance](/static/content/tds/bias-variance.png)

---

=======

---

## Allure des courbes

![Courbes](/static/content/tds/courbes.png)

---

## Carte de chaleur

![Heatmap](/static/content/tds/heatmap.png)

---

## Apprentissage supervisé

- Prédire une valeur en fonction d'une observation
- S'entraîner sur des données réelles (*train*)
- Evaluation d'une méthode via une validation croisée (*test*)

---

## Dilemne biais-variance

![bias-variance](/static/content/tds/bias-variance.png)

---

>>>>>>> 6d5107c119acc8ddd0acd36b171cc0c9a609d5ad
## Défis

- Quelle modélisation ?
- Quelle méthode supervisée choisir ?
- Pas beaucoup de données au départ
- Difficile d'avoir une météo précise
- Temps d'apprentissage non négligeable
- Combien de données considérer ?

---

## Modélisation

- Les données statiques sont propres à l'objet étudié (une station)
- Les données dynamiques varient (wouah)
- Différence anodine mais extrêmement importante pour la modélisation
- Possibilité de prédire pour une ville ou pour une station

---

<<<<<<< HEAD
## Arbre de décision (1)

![Tree](/static/content/tds/tree.png)

---

## Arbre de décision (2)

![Tree2](/static/content/tds/tree2.png)

---

## Roulement

- On assigne un prédicteur à chaque station
- On relance les prédicteurs chaque semaine
- On stocke les prédicteurs dans un dossier
- D'autres outils peuvent appeller ces prédicteurs

---

## Dilemne d'optimisation

- Les tendances changent au fur et à mesure du temps
- On rafraîchit les prédicteurs tous les combien ?
- On entraîne le modèle sur combien de jours en arrière ?

---

## Validation croisée temporelle

- On sépare le jeu de données en deux
- On entraîne le modèle sur la première partie et on prédit le deuxième
- Deux paramètres **externes au modèle** à optimiser

---

## Courbes d'erreurs

![Erreurs](/static/content/tds/erreurs.png)

---

# Utilisations

---

## Poser/prendre un vélo

- Des scénarios sont proposés à l'utilisateur
- L'utilisateur rentre des paramètres
- On utilise les prédictions pour trouver une station appropriée

---

## Choisir une station

- Minimisation de la distance et du risque
- Choix d'un sous-ensemble de stations avec MongoDB
- Google Distance Matrix pour estimer les durées
- Estimation de la météo

---

## Prendre puis poser un vélo

- Partir du point A
- Prendre un vélo à la station 1
- Poser le vélo à la station 2
- Aller au point B

---

## Acheminer des vélos de façon optimale

- Domaine pas du tout automatisé
- Clairement un besoin
- Patterns réguliers
- Nécessite une couche supplémentaire d'optimisation

---

## Modélisation en graphes

---

## Gestion de l'erreur commise

- On intègre l'erreur de façon pessimiste
- Les utilisateurs sont sûrs d'être satisfaits
- Les prédictions pour les acheminements sont accentuées

---

# Conclusion

---

## Structure du projet

- Architecture microservices
- On réfléchit en termes de composants
- Tout se passe sur GitHub

---

## Déploiement

- Tourne sur un droplet Digital Ocean à 20$ mensuels
- 2GB RAM, 2 coeurs, 40GB SSD, 3TB taux de transfert
- On réfléchit à Docker

---

## Stabilité

![CPU](/static/content/tds/cpu.png)

=======
## Arbre de décision

---

## Roulement

- On assigne un prédicteur à chaque station
- On relance les prédicteurs chaque semaine
- On stocke les prédicteurs dans un dossier
- D'autres outils peuvent appeller ces prédicteurs

---

## Courbes d'erreurs

![Erreurs](/static/content/tds/erreurs.png)

---

## Gestion de l'erreur commise

---

## Améliorations envisageables

---

# Utilisations

---

## Poser/prendre un vélo

---

## Gérer les pénuries

---

# Conclusion

---

## Structure du projet

>>>>>>> 6d5107c119acc8ddd0acd36b171cc0c9a609d5ad
---

## Conseils

- Utiliser des normes (geoJSON, ISO 8601 pour les dates...)
- Keep it simple, stupid!
- Réflechir à la structure du projet = investissement
- Décomposer en microservices
- Généraliser les traitements le plus possibles
- Pas besoin d'un bazooka pour tuer une mouche

---

<<<<<<< HEAD
## API

- Redistribution de la donnée uniformisée
- Possibilité de faire une prédiction
- Données libres <3

---

=======
>>>>>>> 6d5107c119acc8ddd0acd36b171cc0c9a609d5ad
## Ouvertures

- Application iPhone/Android
- Notifications pour signaler les vélos cassés
- Granulariser les prédictions
- Ajouter des villes!
<<<<<<< HEAD

---

## Liens

- github.com/OpenBikes
- github.com/MaxHalford
- github.com/Belekkk

L'aide est la bienvenue!
=======
>>>>>>> 6d5107c119acc8ddd0acd36b171cc0c9a609d5ad
