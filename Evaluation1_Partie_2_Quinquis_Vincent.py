# Question 1
def grille():
    
    g=[["*","*","*"], ["*","*","*"], ["*","*","*"]]
    return g
    
def affichage(liste):
    for i in liste:
        print(i)

# Question 2
def X(liste,x,y):
    liste[y][x]="X"

def O(liste,x,y):
    liste[y][x]="O"

# Question 3
def verification(liste):
    for lignes in liste:
        if lignes[0] !='*':
            if lignes[0]==lignes[1] and lignes[1]==lignes[2]:
                return True

    for colonnes in range(len(liste)):
        if liste[0][colonnes] !='*':
            if liste[0][colonnes]==liste[1][colonnes] and liste[1][colonnes]==liste[2][colonnes]:
                return True

    if liste[0][0]!='*' and liste[0][2]!='*':
        if liste[0][0]==liste[1][1] and liste[1][1]==liste[2][2]:
            return True
        elif liste[2][0]==liste[1][1] and liste[1][1]==liste[0][2]:
            return True

    else:
        return False

#Question 4
def complete(liste):
    for y in liste:
        if '*' in y:
            return False 
    return True

# Question 5
def Tic_Tac_Toe():
    Grille=grille()
    Fini=False
    complet=False
    while Fini==False and complet==False:

        affichage(Grille)
        Fini=verification(Grille)
        complet=complete(Grille)
        if Fini==True or complet==True:
            break
        print("Au joueur X")
        ligne=int(input("Sur quelle ligne veut tu jouer ? (1 à 3) : "))-1
        colonne=int(input("Sur quelle colonne veut tu jouer ? (1 à 3) : "))-1
        X(Grille,colonne,ligne)
        affichage(Grille)
        Fini=verification(Grille)
        complet=complete(Grille)
        if Fini==True or complet==True:
            break

        print("Au joueur O")
        ligne=int(input("Sur quelle ligne veut tu jouer ? (1 à 3) : "))-1
        colonne=int(input("Sur quelle colonne veut tu jouer ? (1 à 3) : "))-1
        O(Grille,colonne,ligne)
        
    
    return "La partie est finie"


if __name__=="__main__":
    print(Tic_Tac_Toe())


    """
    Exemple pour la fonction "complete":

    Grille1=[["X","O","O"], ["O","*","X"], ["O","X","O"]]
    print(Grille1)
    print(complete(Grille1))
    """
# Question 6:
"""
Il suffirait de faire une grille plus grande et de changer les conditions de verification
afin qu'elles se valident avec une ligne/colonne/diagonale de 4 et non de 3
"""