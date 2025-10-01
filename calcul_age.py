annee_naissance = int(input("Année de naissance ?"))
age_actuel = 2025 - annee_naissance
print("Ton age cette année est de", age_actuel, "ans")
if age_actuel < 18 :
    print("Mineur cette année")
