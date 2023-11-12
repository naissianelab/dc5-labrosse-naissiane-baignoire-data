def convertir_ctr_en_pourcentage(ctr):

    if not isinstance(ctr, (int, float)):
        print("Erreur : Le CTR doit être un nombre.")
        return None
    
    pourcentage_ctr = ctr * 100
    return pourcentage_ctr

ctr = 0.086

resultat = convertir_ctr_en_pourcentage(ctr)

print(f"CTR : {ctr} en pourcentage : {resultat}%")