depenses_mensuelles = [800, -120, 1200, 87, 0.5, 368, 489, 355, 700, 900, "ok", 886]
depenses_totales = 0

for depense_mensuelle in depenses_mensuelles:
    if isinstance(depense_mensuelle, (int, float)):
        depenses_totales += depense_mensuelle

print(f"Les dépenses marketing de l'années sont de : {depenses_totales}")