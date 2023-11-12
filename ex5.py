liste_clients = []

for i in range(1, 51):
    nom_client = f"Client{i}"
    email_client = f"client{i}@example.com"
    montant_depense_client = 1000 + i * 50
    
    client = {"nom": nom_client, "email": email_client, "montant_depense": montant_depense_client}
    
    liste_clients.append(client)

for client in liste_clients:
    print(f"Nom: {client['nom']}, Email: {client['email']}, Montant dépensé: {client['montant_depense']}")