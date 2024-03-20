import sqlite3
import json
import os
import sys

def get_data_fromjson(number):
    json_file = [f for f in os.listdir('log')]
    with open('log/'+json_file[int(number)-1], 'r') as file :
        data = json.load(file)
    return data 

def clear_db():
    conn = sqlite3.connect('DB/info.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM infopc;')
    conn.commit()
    conn.close()
    print('Database cleared')

def insert_data(data):
    conn = sqlite3.connect('DB/info.db')
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
            INSERT INTO infopc (date_heure, utilisation_cpu, utilisation_disque, utilisation_ram, nbr_utilisateurs, nb_processus)
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (row['date_heure'], row['utilisation_cpu'], row['utilisation_disque'], row['utilisation_ram'], row['nbr_utilisateurs'], row['nb_processus']))
    conn.commit()
    conn.close()
    print('Data restored in info.db')
    
def main(number='1'):
    clear_db()
    data = get_data_fromjson(number)
    insert_data(data)
    
#on récupère le nombre du fichier en argument

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python RestoreJson.py <number>')
        sys.exit(1)
    main(sys.argv[1])