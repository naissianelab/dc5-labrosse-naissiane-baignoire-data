nom_entrepise = input("Rentrez le nom de l'entreprise : ")
nombre_clients = int(input("Rentrez le nombre de clients : "))
revenu_moyen = float(input("Rentrez le revenu moyen par client : "))

revenu_total = revenu_moyen * nombre_clients

print(f"Le revenu total de l'entreprise est de : {revenu_total} ")