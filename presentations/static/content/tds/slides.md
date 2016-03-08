# Plan

- Présentation générale
- Collecte des données
- Visualisation
- Stockage
- Prédiction
- Proposition de trajet

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

- Max **Halford**
- Axel **Bellec**
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

# Collection des données

---

## Les données, concrètement

- Le nombre de vélos et de places
- Le moment de la mise à jour pour chaque station
- Autant de villes que de formats de données (ou presque)
- Besoin d'uniformiser les données le plut tôt possible pour généraliser les traitements par la suite

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
    data = requests.get(url, apiKey=keys.jcdecaux, contract='Toulouse')
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

- On définit une fonction de *récupération* et de *normalisation* par fournisseur de données
- Une file d'attente parallèle (RabbitMQ) gère les appels aux fonctions à un *intervalle régulier* (1 minute suffit)
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

## Quand un utilisateur accède à une URL 
### LeafletJS...

- ouvre le fichier geoJSON de la ville,
- centre la carte sur la ville,
- parcourt chaque station et l'affiche sur la carte.

---

## Avantages de Flask + LeafletJS

- Un seul fichier pour toutes les cartes
- Rapide à développer
- Les deux sont très utilisés donc beaucoup de posts sur StackOverflow

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
- Hype

---

# Avant

![Avant](/static/content/tds/avant.png)

---

# Après

![Après](/static/content/tds/apres.png)

---

# Prédiction

---

## Exemple de données



---

## Exemple de courbe

---

## Différences entre données statiques et données dynamiques

- Les données statiques sont propres à l'objet étudié (une station)
- Les données dynamiques changent (wouah)
- Différence anodine mais ô combien importante en modélisation.


---

# Conseils

- Utiliser des normes (geoJSON, ISO 8601 pour les dates...)
- Keep it simple, stupid!
- Prenez le temps de réfléchir à la structure du projet -> temps gagné par la suite
- Généralisez vos fonctions le plus possible, uniformisez vos données le plus tôt possible
- Pas besoin d'un bazooka pour tuer une mouche

---

# Contact 

## GitHub

- `github.com/MaxHalford`
- `github.com/belekkk`

<br>
## Site web

- `maxhalford.com`
- `axelbellec.fr`

---

### Vous pouvez nous retrouver sur Twitter

# @OpenBikes_

<figure>
    <p style="text-align:center">
        <img src="/static/content/tds/wordcloud.gif" alt="mask_wordcloud" style="background:none; border:none; box-shadow:none;height=30%;width=auto;">
    </p>
</figure>
