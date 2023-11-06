liste_nombres = [10 , 9, 7, 6, 5, 4, 3 , -2, 11, "ok"]

maximum = liste_nombres[0]

for element in liste_nombres:
    if isinstance(element, (int, float)):
        if element > maximum:
            maximum = element

minimum = liste_nombres[0]

for element in liste_nombres:
    if isinstance(element, (int, float)):
        if element < minimum:
            minimum = element

somme = 0
compteur = 0

for element in liste_nombres:
    if isinstance(element, (int, float)):
        somme += element
        compteur += 1

moyenne = somme / compteur

if compteur > 0:
    print("Le nombre maximum de la liste est : ", maximum)
    print("Le nombre minimum de la liste est : ", minimum)
    print("La moyenne de la liste est : ", moyenne)
else:
    print("La liste ne contient aucun nombre valide.")