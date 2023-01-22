def isGeometric(liste):
    if type(liste) == list and liste != []: 
        if liste[0] != 0 :
            raison = liste[1]/liste[0]
            for i in range(1, len((liste))-1) :
                if liste[i] != 0 :
                    if (liste[i+1]/liste[i]) != raison :
                        return False
                else :
                    return False
            return True
        else :
            return not(any(liste))
    else :
        return False
