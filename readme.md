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

### Auteurs

- [Buren Arthur]