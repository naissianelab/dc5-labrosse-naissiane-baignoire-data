liste_clients = []

for i in range(1, 51):
    nom_client = f"Client{i}"
    email_client = f"client{i}@example.com"
    montant_depense_client = 30 + i * 4

    client = {"nom": nom_client, "email": email_client, "montant_depense": montant_depense_client}
    
    liste_clients.append(client)

montant_total = 0

for client in liste_clients:
    montant_depense_client = client['montant_depense']
    if isinstance(montant_depense_client, (int, float)):
        montant_total += montant_depense_client

print(f"Le montant total dépensé par les clients est de {montant_total}€")