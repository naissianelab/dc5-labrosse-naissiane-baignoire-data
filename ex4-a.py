def convertir_ctr_en_pourcentage(ctr):
    pourcentage_ctr = ctr * 100
    return pourcentage_ctr

ctr = 0.086

resultat = convertir_ctr_en_pourcentage(ctr)

print(f"CTR : {ctr} en pourcentage : {resultat}%")