import random

print("\n            Début de partie de Pierre/Feuille/Ciseaux")

print("\n------------------------------------------------------------\n")

def partie():
    
    print("                      Faites votre choix : \n")
    print("              Pierre = P, Feuille = F, Ciseaux = C\n")

    allChoices = ["P","F","C"]

    allLiterralChoices = ["Pierre","Feuille","Ciseaux"]

    userChoice = str(input())

    while allChoices.count(userChoice) == 0 :
        print("                      Mauvaise saisie ! \n")
        print("            Rappel : Pierre = P, Feuille = F, Ciseaux = C\n")
        userChoice = str(input())

    indexComputerChoice = random.randint(0,2)

    indexUserChoice = allChoices.index(userChoice)

    print("\n              L'ordinateur a choisi : " + str(allLiterralChoices[indexComputerChoice]))
    print("\n                 Vous avez choisi : " + str(allLiterralChoices[indexUserChoice]))

    if (indexUserChoice==0 and indexComputerChoice == 2) or (indexUserChoice==1 and indexComputerChoice == 0) or (indexUserChoice==2 and indexComputerChoice == 1):
        print("\n                          Gagné !")
    elif indexComputerChoice == indexUserChoice:
        print("\n                         Egalite !")
    else:
        print("\n                          Perdu !")

game = 1

while game == 1 :
    partie()
    print("\n                   Voulez-vous rejouer ?")
    print("0 = Non et 1 = Oui")
    replay = int(input())
    game = replay

print("                         Au revoir !")