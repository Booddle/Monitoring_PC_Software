import sqlite3



# connexion à la base de données
conn = sqlite3.connect('/home/arthur/adminsys/DB/info.db')
cursor = conn.cursor()

# récupération des données 
cursor.execute('SELECT * FROM alert;')
data = cursor.fetchall()

# fermeture de la connexion
conn.close()

#donnée dans un json
json_data = []
for row in data:
    json_data.append({'date': row[1], 'ref': row[2], 'title': row[3], 'status': row[4]})
    
#envoie des données dans le fichier  xml
with open('/var/www/html/alert.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<alerts>\n')
    for row in json_data:
        f.write('  <alert>\n')
        f.write('    <date>{}</date>\n'.format(row['date']))
        f.write('    <ref>{}</ref>\n'.format(row['ref']))
        f.write('    <title>{}</title>\n'.format(row['title']))
        f.write('    <status>{}</status>\n'.format(row['status']))
        f.write('  </alert>\n')
    f.write('</alerts>\n')
