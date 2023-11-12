liste_clients = []

for i in range(1, 51):
    nom_client = f"Client{i}"
    email_client = f"client{i}@example.com"
    montant_depense_client = 30 + i * 4
    
    client = {"nom": nom_client, "email": email_client, "montant_depense": montant_depense_client}
    
    liste_clients.append(client)

for client in liste_clients:
    if client['montant_depense'] > 100:
        print(f"Nom: {client['nom']}, Email: {client['email']}, Montant dépensé: {client['montant_depense']}€")