import random

print("\n                 Début de partie de Chaud-Froid")

print("\n------------------------------------------------------------\n")

print("  Entrez les bornes d'encadrement de la valeur à chercher : \n")

print("  Valeur minimum :")

min = int(input())

print(" \n Valeur minimum :")

max = int(input())

toGuess = random.randint(min,max)

valueTry = 1000

print("\n  Entrez une valeur pour deviner celle choisie par le jeu : \n")

valueTry = int(input())

while valueTry != toGuess :

    print("  Dommage, continuez de chercher ! \n")

    print("  Entrez une valeur pour deviner celle choisie par le jeu : \n")

    lastTry = valueTry

    valueTry = int(input())

    if valueTry > max or valueTry < min :
        print("                 \nVous etes en dehors des bornes.")
        print("      \nVeuillez saisir une valeur entre "+str(min)+" et "+str(max)+".\n")
    elif abs(toGuess - valueTry) < abs(toGuess-lastTry) :
        print("                     \nVous chauffez ! \n")
    elif abs(toGuess - valueTry) == abs(toGuess-lastTry) :
        print("                \nMeme temperature. \n")
    else :
        print("                \nVous refroidissez... \n")

print("         \nVous avez trouvé !\n")
print("         La valeur à trouver etait bel et bien "+str(toGuess)+".\n")
