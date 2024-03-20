#!/bin/bash

#on veut récuperer l'utilisation CPU DISQUE RM et la temp C°, le nombre de process, le nombre d'utilisateur connecté




#on compte le nombre de processus en cours d'exécution en bash
nbProcessus=$(ps -ef | wc -l)
#on récupère l'utilisation CPU en python
utilisationCPU=$(python3 -c "import psutil; print(psutil.cpu_percent(interval=1))")
#on récupère l'utilisation DISQUE en python
utilisationDISQUE=$(python3 -c "import psutil; print(psutil.disk_usage('/').percent)")
#on récupère l'utilisation RAM en python
utilisationRAM=$(python3 -c "import psutil; print(psutil.virtual_memory().percent)")
#on récupère la température en python
# tempCPU=$(python3 -c "import psutil; print(psutil.sensors_temperatures()['coretemp'][0].current)")
#on compte le nombre d'utilisateur connecté
nbUtilisateur=$(who | wc -l)

#on stock les valeurs dans un fichier txt
# echo "Utilisation CPU: $utilisationCPU %" > info/infosonde.txt
# echo "Utilisation DISQUE: $utilisationDISQUE %" >> info/infosonde.txt
# echo "Utilisation RAM: $utilisationRAM %" >> info/infosonde.txt
# # echo "Température CPU: $tempCPU °C" >> info/infosonde.txt
# echo "Nombre de processus: $nbProcessus" >> info/infosonde.txt
# echo "Nombre d'utilisateur connecté: $nbUtilisateur" >> info/infosonde.txt

#on crée la base de donnée si elle n'existe pas
sqlite3 /home/arthur/adminsys/DB/info.db "CREATE TABLE IF NOT EXISTS infopc(id INTEGER PRIMARY KEY, utilisation_cpu REAL, utilisation_disque REAL, utilisation_ram REAL, nbr_utilisateurs INTEGER, nb_processus INTEGER);"

#on envoie les valeurs à la base de donnée
sqlquery="INSERT INTO infopc(utilisation_cpu, utilisation_disque, utilisation_ram, nbr_utilisateurs, nb_processus) VALUES ($utilisationCPU, $utilisationDISQUE, $utilisationRAM, $nbUtilisateur, $nbProcessus);"

sqlite3 /home/arthur/adminsys/DB/info.db "$sqlquery"

#compter les lignes de la bdd
row=$(sqlite3 /home/arthur/adminsys/DB/info.db "SELECT COUNT(*) FROM infopc;")
#si on a plus de 25 lignes on supprime la première
if [ "$row" -gt 25 ]
then
    sqlite3 /home/arthur/adminsys/DB/info.db "DELETE FROM infopc WHERE date_heure = (SELECT MIN(date_heure) FROM infopc);"
fi

#on va sauvegarder les valeurs dans un fichier json via un script python si -s est passé en argument
if [ "$1" = "-s" ]
then
    python3 /home/arthur/adminsys/script_python/SaveJson.py
fi

#on va restaurer les valeurs dans la bdd via un script python si -r est passé en argument
#si il n'y a pas de nombre on prend la dernière sauvegarde sinon on prend la sauvegarde correspondante 

if [ "$1" = "-r" ]
then
    if [ -z "$2" ]
    then
        python3 /home/arthur/adminsys/script_python/RestoreJson.py
    else
        python3 /home/arthur/adminsys/script_python/RestoreJson.py "$2"
    fi
fi

#on récupère actualise la bdd avec le site cert.ssi.gouv.fr

python3 /home/arthur/adminsys/CERTinDB/getcert.py

# on va réaliser un graphe de bdd via un script python

python3 /home/arthur/adminsys/script_python/graph.py

# on va réaliser un script qui contrôle l'historique de la bdd pour voir si il y a des alertes

#python3 /home/arthur/adminsys/mail/alert.py

if [ "$1" = "-m" ]
then
    python3 /home/arthur/adminsys/mail/editmail.py
fi

#on va réaliser un script qui transforme la table alert en xml et la met dans www/html

python3 /home/arthur/adminsys/script_python/alert.py