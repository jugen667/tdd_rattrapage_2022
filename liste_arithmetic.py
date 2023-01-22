def isArithmetic(liste):
    if type(liste) == list and liste != []: 
        raison = liste[1]-liste[0]
        for i in range(1, len((liste))-1) :
            if (liste[i+1]-liste[i]) != raison :
                return False
        return True
    else :
        return False
