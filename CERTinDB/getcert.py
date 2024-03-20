import requests
from bs4 import BeautifulSoup
import sqlite3

def get_cert_alert_info(alert):
    info = {}
    info['date'] = alert.find(class_='item-date').text.strip()
    info['ref'] = alert.find(class_='item-ref').text.strip()
    info['title'] = alert.find(class_='item-title').text.strip()
    info['status'] = alert.find(class_='item-status').text.strip()
    return info

url = "http://www.cert.ssi.gouv.fr/"
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
soup.prettify(formatter=None)
conn = sqlite3.connect('DB/info.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS alert (id INTEGER PRIMARY KEY, date TEXT, ref TEXT UNIQUE, title TEXT, status TEXT)')


alerts = soup.select('.item.cert-alert')
for alert in alerts:
    info = get_cert_alert_info(alert)
    #print('Alerte:', info['ref'] + ' - ' + info['title'])

    # on vérifie si l'alerte n'est pas déjà dans la base
    cursor.execute('SELECT * FROM alert WHERE ref=?', (info['ref'],))
    existing_alert = cursor.fetchone()
    if existing_alert:
        #print('Alerte déjà dans la base\n ')
        continue
    
    cursor.execute('INSERT INTO alert (date, ref, title, status) VALUES (?, ?, ?, ?)', (info['date'], info['ref'], info['title'], info['status']))
    #print('Alerte ajoutée à la base\n ')
    
conn.commit() 
conn.close()