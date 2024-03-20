

input("voulez-vous modifier le mail ?(y/n) ")

if "y" in input :
    with open("mail/mail.txt", "w") as file:
        subject = '''\
            Subject: '''
        subject += input("sujet du mail : ")
        subject += "\n\n"
        subject += input("message du mail : ")
        file.write(subject)

input("voulez-vous modifier les alertes ?(y/n) ")

if "y" in input :
    with open("mail/checkalert.txt", "w") as file:
        input("alerte cpu ?(y/n) ")
        if "y" in input :
            file.write("cpu ")
            a=input("% pour l'alerte?")
            file.write(a+"\n")
        input("alerte ram ?(y/n) ")
        if "y" in input :
            file.write("ram ")
            a=input("% pour l'alerte?")
            file.write(a+"\n")
        input("alerte disk ?(y/n) ")
        if "y" in input :
            file.write("disk ")
            a=input("% pour l'alerte?")
            file.write(a+"\n")
        input("alerte number_of_users ?(y/n) ")
        if "y" in input :
            file.write("number_of_users ")
            a=input("nbr pour l'alerte?")
            file.write(a+"\n")
        input("alerte nbr_process ?(y/n) ")
        if "y" in input :
            file.write("nbr_process ")
            a=input("nbr pour l'alerte?")
            file.write(a+"\n")

