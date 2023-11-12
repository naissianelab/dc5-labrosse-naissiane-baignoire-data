def calculer_factoriel(nombre):

    if not isinstance(nombre, int) or nombre < 0:
            print("Erreur : Le nombre doit être un entier positif.")
            return None

    resultat = 1

    for i in range(1, nombre + 1):
        resultat *= i

    return resultat

nombre = 3

resultat = calculer_factoriel(nombre)


print(f"Le factoriel du nomre {nombre} est {resultat}")