

## Plan


<div id="contentBox" style="margin:0px auto; width:100%">

<div id="column1" style="float:left; margin:0; width:50%;" markdown="1">
<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/wordcloud.gif" alt="wordcloud" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>
**#openbikes**
</div>

<div id="column2" style="text-align:left;float:left; margin:0;width:50%;" markdown="1">
<br>
- **<font color="darkblue">Présentation générale</font>** <br>
- Collection des données <br>
- Visualisation <br>
- Stockage <br>
- Prédiction <br>
- Utilisations <br>
- Bonnes pratiques 
</div>
</div>

---

## **OpenBikes** c'est quoi ?

- **Visualiser** les vélibs en (quasi) temps réel
- Faire de la **prédiction** pour optimiser les trajets (gratuitement)
- **Conseiller** les villes pour **acheminer** les vélos entre stations (depuis le concours)

---

#### **http://openbikes.co**

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

Étudiants en Data Science

<div style="float:left;margin:0 10px 10px 0" markdown="1">
    ![axelbellec](/static/content/tds/maxhalford.jpg)
</div>

<div style="float:right;margin:0 10px 10px 0" markdown="1">
    ![axelbellec](/static/content/tds/axelbellec.jpg)
</div>

<div style="float:left;margin:0 10px 10px 0" markdown="1">
    Max **Halford** <br>
    `maxhalford.com`
</div>

<div style="float:right;margin:0 10px 10px 0" markdown="1">
    Axel **Bellec** <br>
    `axelbellec.fr`
</div>

---

## Notre formation

### Université Paul SABATIER - Toulouse III

M1 Statistiques et Informatique Décisionnelle  

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/sid.gif" alt="sid" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

### Prix **Open Data Toulouse Métropole**

![Concours](/static/content/tds/concours.png)

---

## Sous le capot

- Un robot codé en **Python** qui collectionne les données toutes les minutes
- Visualisation avec **Flask** et **LeafletJS**
- Stockage des données avec **MongoDB**
- Prédiction avec **sklearn**
- Un ensemble de règles et un stack basé sur l'**API Google Maps** pour établir des trajets
- Redistribution des données via une **API**

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/souslecapot.gif" alt="souslecapot" style="width: 80%;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Flowchart

![Flowchart](/static/content/tds/flowchart.jpg)

---

## Plan

- Présentation générale
- **<font color="darkblue">Collection des données</font>**
- Visualisation
- Stockage
- Prédiction
- Utilisations
- Bonnes pratiques

---

## Les données, concrètement

- Le nombre de vélos + le moment de la mise à jour pour chaque station
- Autant de villes que de formats de données (presque)
- Besoin d'**uniformiser les données** le plut tôt possible pour **généraliser les traitements** par la suite

---

## Sources

- *Bixi*, *JCDecaux*, *Citibike*, *Divvy*, *Keolis*, *Nextbike*, *Niceride*, *Santander*, *Velobleu*... 
- 25 sources de données pour le moment
- Que des données ouvertes et illimitées...
- Mais en différents formats!

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


![horloge](/static/content/tds/automatisation.jpg)

- Fonction de **récupération** et de **normalisation** par fournisseur de données
- File d'attente parallèle (RabbitMQ) gérant les appels aux fonctions à un **intervalle régulier**

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/rabbitmq.gif" alt="rabbitmq" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Plan

- Présentation générale
- Collection des données
- **<font color="darkblue">Visualisation</font>**
- Stockage
- Prédiction
- Utilisations
- Bonnes pratiques


---

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/leaflet.png" alt="leafletjs" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

- Permet d'afficher des points, des lignes et des polygones
- Grande communauté, beaucoup de plugins, très maintenu
- Compatible avec tous les formats de données populaires



---

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/flask.png" alt="flask" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

- Framework Python pour développer un site web
- Très "Pythonesque", extrêmement modulable
- Simple, rapide, documenté...

---

## Pour chaque ville, toutes les minutes, on...

- récupère les données pour la ville,
- les sauvegarde en fichier geoJSON,
- garde seulement les données les plus récentes.

---

## Quand un utilisateur accède à une URL, **LeafletJS**...

- ouvre le fichier geoJSON de la ville,
- centre la carte sur la ville,
- parcourt chaque station et l'affiche sur la carte.

---

## Avantages de **Flask** + **LeafletJS**

- Un seul fichier pour toutes les cartes.
- Rapide à apprendre, développement rapide.
- Les deux sont très utilisés donc beaucoup de posts sur StackOverflow :)

---

## Plan

- Présentation générale
- Collection des données
- Visualisation
- **<font color="darkblue">Stockage</font>**
- Prédiction
- Utilisations
- Bonnes pratiques

---

## Que nous faut-il ?

- <i class="fa fa-clock-o"></i> Date et heure
- <i class="fa fa-bicycle"></i> Nombre de vélos
- <i class="fa fa-child"></i> Nombre de places
- <i class="fa fa-map-marker"></i> Position géographique
- <i class="fa fa-cloud"></i> Météo

---

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/mongodb.png" alt="mongodb" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

- Pas besoin d'un schéma compliqué
- Extrêmement simple à mettre en place
- Très fort en écriture (WiredTiger)
- Pour s'entraîner/changer...

---

# Avant

```json
    {
        "_id": ObjectID("5304c94ba44d082cff0b5d9b"),
        "number": 55,
        "name": "00055- ST SERNIN G. ARNOULT",
        "address": "2 RUE GATIEN ARNOULT",
        "position": {
            "lat": 43.6089519604964053,
            "lon": 1.4410035987261980
        },
        "banking": true,
        "bonus": false,
        "status": "OPEN",
        "contract_name": "Toulouse",
        "bike_stands": 15,
        "available_bike_stands": 14,
        "available_bike": 1,
        "last_update" : NumberLong(1392822479000)
    }
```


---

# Après

```json
{
    "_id": "2016-02-15",
    "u": [
        {
            "i" : [
                {
                    "m": "23:29:15",
                    "b": 8,
                    "s": 12
                },
                {
                    "m": "23:39:17",
                    "b": 8,
                    "s": 12
                }
            ],
            "n" : "02 - LES HALLES"
        },
        // etc
    ]
}
```

---

## Plan

- Présentation générale
- Collection des données
- Visualisation
- Stockage
- **<font color="darkblue">Prédiction</font>**
- Utilisations
- Bonnes pratiques

---

## Objectifs

- Aider un utilisateur à choisir une station
- Optimiser l'acheminement des vélos

---

## Exemple de données

![Donnees](/static/content/tds/donnees.png)

---

**Nombre de vélos** disponibles dans **2 stations différentes** de Toulouse

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/courbes.png" alt="courbes" style="width: 80%;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Carte de chaleur
<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/heatmap.png" alt="heatmap" style="width: 80%;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Apprentissage supervisé

- Prédire une valeur en fonction d'une observation
- S'entraîner sur des données réelles (**train**)
- Evaluation d'une méthode via une validation croisée (**test**)

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/vc.png" alt="vc" style="width: 450px; background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Dilemne biais-variance

![bias-variance](/static/content/tds/bias-variance.png)

---

## Défis

- Quelle modélisation ?
- Quelle méthode supervisée choisir ?
- Pas beaucoup de données au départ
- Difficile d'avoir une météo précise
- Temps d'apprentissage non négligeable
- Combien de données considérer ?

---

## Modélisation

- Les données **statiques** sont propres à l'objet étudié (une station)
- Les données **dynamiques** sont les seuls à prendre en compte
- Différence anodine mais extrêmement importante pour la modélisation
- Possibilité de prédire pour une ville ou pour une station

---

## Choix des variables

- Jour de la semaine
- Heure
- Minute
- Données météo

<br>
**Pas besoin de données géographiques !**

---

## Arbre de décision (1)

![Tree2](/static/content/tds/decisiontree.jpg)

---

## Arbre de décision (2)

![Tree2](/static/content/tds/decisiontree2.jpg)

---

## Dilemne d'optimisation

- Les tendances changent au fur et à mesure du temps
- On rafraîchit les prédicteurs selon quelle fréquence ?
- On entraîne le modèle sur combien de jours en arrière ?

---

## Validation croisée temporelle

- On sépare le jeu de données en deux
- On entraîne le modèle sur la première partie et on prédit le deuxième
- Deux paramètres **externes au modèle** à optimiser

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/va_temp.png" alt="va_temp" style="height: 300px;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Validation croisée temporelle



<iframe width="900" height="450" frameborder="0" scrolling="no" src="https://plot.ly/~MaxHalford/188.embed?share_key=qgNjdULzOnQIzl9tUFL5cC"/>

---

## Courbes d'erreurs

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/erreurs.png" alt="erreurs" style="width:80%;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Roulement

- On assigne un prédicteur à chaque station
- On relance les prédicteurs chaque semaine
- On stocke les prédicteurs dans un dossier
- D'autres outils peuvent appeller ces prédicteurs
- La prédiction devient un **microservice**

---

## Plan

- Présentation générale
- Collection des données
- Visualisation
- Stockage
- Prédiction
- **<font color="darkblue">Utilisations</font>**
- Bonnes pratiques

---

## Poser/prendre un vélo

- Des **scénarios** sont proposés à l'utilisateur
- L'utilisateur rentre des paramètres
- On utilise les prédictions pour trouver une station **appropriée**
- Minimisation de la **distance** et du **risque**

---

## Choisir une station

### Gestion du risque

- Prédiction en temps réel
- Besoin d'estimer le temps d'arrivée
- Besoin de la météo

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/owm.png" alt="owm" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Choisir une station

### Gestion de la distance

- Google Distance Matrix pour estimer les durées
- Choix d'un sous-ensemble de stations avec MongoDB

---

## Scénario possible

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/cheminement.png" alt="cheminement" style="height: 500px;background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Acheminer des vélos de façon optimale

- Domaine pas du tout automatisé
- Besoin clair
- Patterns réguliers
- Nécessite une couche supplémentaire d'optimisation


---

## Gestion de l'erreur commise

- On intègre l'erreur de façon pessimiste
- Les utilisateurs sont sûrs d'être satisfaits
- Les prédictions pour les acheminements sont accentuées

<br>

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/ic.png" alt="ic" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Plan

- Présentation générale
- Collection des données
- Visualisation
- Stockage
- Prédiction
- Utilisations
- **<font color="darkblue">Bonnes pratiques</font>**

---

## Structure du projet

- Architecture **microservices**
- On réfléchit en termes de composants
- Tout se passe sur **GitHub**
- Travail collaboratif au travers de **Slack**

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/github_slack.gif" alt="github_slack" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>


---

## Déploiement
### Ressources matérielles

- Tourne sur un droplet *Digital Ocean* à 20$ mensuels
- 2GB RAM, 2 coeurs, 40GB SSD, 3TB taux de transfert
- On réfléchit à un déploiement avec Docker

<figure>
  <p style="text-align:center">
  <img src="/static/content/tds/digitalocean.png" alt="digitalocean" style="background:none; border:none; box-shadow:none;">
  </p>
</figure>

---

## Déploiement
### Stabilité

![CPU](/static/content/tds/cpu.png)

---

## API

- Redistribution de la donnée uniformisée
- Possibilité de faire une prédiction
- Données libres

---

## API

<div class="stretch">
  <iframe src="http://docs.openbikes.apiary.io/" height="100%" width="100%" />
</div>

---

## API
### Exemple de réponse

```json
{
  "bikes": {
    "quantity": 0.0,
    "std": 2
  },
  "city": "Toulouse",
  "spaces": {
    "quantity": 17.0,
    "std": 2
  },
  "station": "00003 - POMME",
  "status": "success",
  "timestamp": 1467993096.0
}
```


---

## Conseils

- Utiliser des normes (`geoJSON`, `ISO8601` pour les dates...)
- Keep it simple, stupid! (KISS)
- Do one thing and do it well (*Philosophie UNIX*)
- Décomposer en microservices
- Généraliser les traitements le plus possibles
- Pas besoin d'une usine à gaz

---

## Ouvertures

- Application iPhone/Android
- Notifications pour signaler les vélos cassés
- Granulariser les prédictions
- Ajouter davantages de villes
- Intégrer d'autres sources de données

---

## Liens

- <i class="fa fa-twitter"></i> twitter.com/@OpenBikes_
- <i class="fa fa-github"></i> github.com/OpenBikes
- <i class="fa fa-github"></i> github.com/MaxHalford
- <i class="fa fa-github"></i> github.com/Belekkk
