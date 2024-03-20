import sqlite3
import subprocess

def check_cpu_usage(size) :
    conn = sqlite3.connect('DB/info.db')
    c = conn.cursor()
    # on récupère les deux dernières lignes
    c.execute("SELECT utilisation_cpu FROM infopc ORDER BY date_heure DESC LIMIT 2")
    result = c.fetchall()
    conn.close()
    if result[0][0] >= size and result[1][0] >= size :
        return True
    else :
        return False
    

def check_ram_usage(size) :
    conn = sqlite3.connect('DB/info.db')
    c = conn.cursor()
    c.execute("SELECT utilisation_ram FROM infopc ORDER BY date_heure DESC LIMIT 2")
    result = c.fetchall()
    conn.close()
    if result[0][0] >= size and result[1][0] >= size :
        return True
    else :
        return False
    

def check_disk_usage(size) :
    conn = sqlite3.connect('DB/info.db')
    c = conn.cursor()
    c.execute("SELECT utilisation_disque FROM infopc ORDER BY date_heure DESC LIMIT 2")
    result = c.fetchall()
    conn.close()
    if result[0][0] >= size and result[1][0] >= size :
        return True
    else :
        return False


def check_number_of_users(nbr) :
    conn = sqlite3.connect('DB/info.db')
    c = conn.cursor()
    c.execute("SELECT nbr_utilisateurs FROM infopc ORDER BY date_heure DESC LIMIT 1")
    result = c.fetchall()
    conn.close()
    if result[0][0] >= nbr :
        return True
    else :
        return False
    

def check_nbr_process(nbr) :
    conn = sqlite3.connect('DB/info.db')
    c = conn.cursor()
    c.execute("SELECT nb_processus FROM infopc ORDER BY date_heure DESC LIMIT 1")
    result = c.fetchall()
    conn.close()
    if result[0][0] >= nbr :
        return True
    else :
        return False
    

# la fonction main va faire un tableau de tous les checks et si un des checks est vrai et qu'il est dans checkalert.txt alors on envoie un mail

def main():
    checkn = ["cpu", "ram", "disk", "number_of_users", "nbr_process"]
    check_functions = [check_cpu_usage, check_ram_usage, check_disk_usage, check_number_of_users, check_nbr_process]
    send_mail = []
    with open("mail/checkalert.txt", "r") as file:
        
        for line in file:
            ligne = line.split()
            if ligne[0] in checkn and check_functions[checkn.index(ligne[0]())](ligne[1]):
                send_mail.append(ligne[0])
                
    
    if send_mail:
        subprocess.run(["python3", "mail/mail.py", *send_mail])
        
        
if __name__ == "__main__" :
    main()