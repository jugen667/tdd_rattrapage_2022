def verif_sudoku(grille):
    # checks
    if not(grille) or type(grille) != list :
        return False
    if len(grille) < 9 :
        return False
    for i in grille :
        if len(i) < 9 or not(i) or type(i) != list :
            return False
    for i in grille :
        for j in i :
            if type(j) != int:
                return False

    # Checking the lines
    for i in range(len(grille)):
        if (len(set(grille[i]))) != 9 :
                return False

    # Checking the columns
    for i in range(len(grille)):
        for k in range(len(grille[i])):
            for j in range(1, len(grille)):
                if grille[i][k] == grille[j][k] and i!=j:
                    return False
              
    # Checking the sub-grids
    for i in range(3):
        for j in range(3):
            subgrid = []
            for k in range(i*3, i*3+3): 
                for l in range(j*3, j*3+3):
                    subgrid.append(grille[k][l])
            if (len(set(subgrid))) != 9 :
                return False
    return True

