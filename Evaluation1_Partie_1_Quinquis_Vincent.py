
def permuter(liste:list, index1:int, index2:int):
    """
    Reponse à la question 1
    """
    memoire=liste[index1]
    liste[index1]=liste[index2]
    liste[index2]=memoire
    return liste

def plus_grand_a_la_fin(liste):
    """
    Reponse à la question 2
    """
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            permuter(liste,i,i+1)
    return liste

def tri_bulle(liste):
    """
    Reponse à la question 3
    """
    """
    Reponse à la question 4:
    Le tri par bulle est lent car il est d'une complexité proportionelle à la longueur de la liste. 
    Comme il doit parcourir toute la liste pour chaque element, plus la liste est grande, plus il sera lent
    """
    for j in range(len(liste)):
        plus_grand_a_la_fin(liste)
    return liste


if __name__=="__main__":
    MyList=[9,7,12,14,33,32]
    print(permuter(MyList,1,2))
    print(plus_grand_a_la_fin(MyList))
    print(tri_bulle(MyList))


