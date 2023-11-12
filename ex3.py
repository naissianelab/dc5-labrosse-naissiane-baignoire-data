import sys

cout_campagne = 400
revenu_campagne = 700

if not isinstance(cout_campagne, (int, float)):
    print("Erreur : Le coût de la campagne n'est pas un nombre.")
    sys.exit()

# Vérification si revenu_campagne est un nombre
if not isinstance(revenu_campagne, (int, float)):
    print("Erreur : Les revenus de la campagne ne sont pas un nombre.")
    sys.exit()

rentabilite_campagne = revenu_campagne - cout_campagne

if rentabilite_campagne > 0:
    print("La campagne a été rentable de ", rentabilite_campagne)

elif rentabilite_campagne < 0:
    print("La campagne n'a pas été rentable de ", rentabilite_campagne)

elif rentabilite_campagne == 0:
    print("La campagne n'a ni généré de profit ni de perte.")