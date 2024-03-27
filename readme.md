### Quel est ce projet ?

Ce projet est un logiciel de monitoring de machine, il permet de monitorer plusieurs données de la machine et de les stocker dans une base de donnée. Il permet aussi de prévenir l'utilisateur par mail si une donnée dépasse un certain seuil. Il dispose également d'une interface web pour visualiser les données.


### SETUP

ajouter main.sh à la crontab:
crontab -e puis à la fin */1 * * * * path/to/main.sh

Bien mettre le fichier web dans un serveur web 

### Fonctionnement

Le logiciel monitorer cette machine automatiquement, il va relever plusieurs donnée comme l'utilisation de la RAM du CPU et du Stockage.
Tout est paramétrable en se baladant dans les fichier.
Pour lancer un fonctionnement spécifique utiliser :
```
./main.sh -arg
```

-s : pour sauvegarder la bdd dans un fichier json

-r X : pour restaurer la bdd depuis une sauvegarde X

-m : pour paramétrer le mail et le monitoring

### Libraries
Python 3 : 
- psutil
- pygal
- sqlite3
- beautifulSoup
- json
- os
- datetime
- sys
- requests

### Auteurs

- [Buren Arthur]
