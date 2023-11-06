phrase_utilisateur = input("Saisi une phrase : ")

phrase_majuscules = ""
for caractere in phrase_utilisateur:
    if 'a' <= caractere <= 'z':
        caractere_majuscule = chr(ord(caractere) - 32)
    else:
        caractere_majuscule = caractere
    phrase_majuscules += caractere_majuscule

print("Voici ta phrase en majuscules : ", phrase_majuscules)

phrase_minuscules = ""
for caractere in phrase_utilisateur:
    if 'A' <= caractere <= 'Z':
        caractere_minuscule = chr(ord(caractere) + 32)
    else:
        caractere_minuscule = caractere
    phrase_minuscules += caractere_minuscule

print ("Voici ta phrase en minusucles : ", phrase_minuscules)

nombre_mots = 1

for caractere in phrase_utilisateur:
    if caractere == ' ':
        nombre_mots += 1

print("Nombre de mots dans la phrase : ", nombre_mots)