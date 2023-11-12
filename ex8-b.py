fichier_texte = 'fichier_texte.txt'

fichier_resultat = 'fichier_resultat.txt'

with open(fichier_texte, 'r') as file:
    contenu = file.read()

    nombre_mots = 0

    est_dans_un_mot = False
    for caractere in contenu:
        if caractere.isalpha():
            est_dans_un_mot = True

        elif est_dans_un_mot:
            nombre_mots += 1
            est_dans_un_mot = False

    if est_dans_un_mot:
        nombre_mots += 1

print(f"Le fichier {fichier_texte} contient {nombre_mots} mots.")

with open(fichier_resultat, 'w') as file_out:
    file_out.write(f"Le fichier {fichier_texte} contient {nombre_mots} mots.")
