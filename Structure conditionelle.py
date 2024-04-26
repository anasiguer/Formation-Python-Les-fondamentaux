'''
Structure conditionelle

if      si              match
else    sinon           case
elif    sinon si

'''
couleur = "jaune"

match couleur:
    case "rouge":
        print("la couleur est rouge")
    case "vert":
        print("la couleur est verte")
    case other:
        print("La couleur n'est pas rouge ou verte") 

if couleur == "rouge":
    print("La couleur est rouge")
elif couleur == "jaune":
    print("La couleur est jaune")
else:
    print("La couleur n'est pas rouge ou jaune")
