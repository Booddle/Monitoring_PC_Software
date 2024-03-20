import sqlite3
import json
import os
import datetime

def get_data():
    conn = sqlite3.connect('DB/info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM infopc;')
    data = cursor.fetchall()
    conn.close()
    return data

def to_json(data):
    data_json = []
    for row in data:
        data_json.append({
            'date_heure': row[0],
            'utilisation_cpu': row[1],
            'utilisation_disque': row[2],
            'utilisation_ram': row[3],
            'nbr_utilisateurs': row[4],
            'nb_processus': row[5],
        })
    return data_json

def write_json(data, number):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S") #trouvé sur internet change l'objet now en string
    with open('log/'+now_str+'.json', 'w') as file:
        json.dump(data, file, indent=4)
        print ('Data saved in data'+number+'.json')


def get_number():
    files = os.listdir('log')
    return str(len(files) + 1)

def main():
    data = get_data()
    data_json = to_json(data)
    number = get_number()
    write_json(data_json, number)
    
if __name__ == '__main__':
    main()
