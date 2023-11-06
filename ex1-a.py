nom_entreprise = input("Rentrez le nom de l'entreprise : ")

try:
    nombre_clients = int(input("Rentrez le nombre de clients : "))
    revenu_moyen = float(input("Rentrez le revenu moyen par client : "))
    
    revenu_total = revenu_moyen * nombre_clients
    print(f"Le revenu total de l'entreprise {nom_entreprise} est de : {revenu_total}")

except ValueError:
    print("Erreur : Vous avez entré un texte au lieu d'un nombre pour le nombre de clients ou le revenu moyen.")