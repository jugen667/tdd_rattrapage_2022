import sudoku

def test_verif_sudoku():
	i = 1
    try :
        assert sudoku.verif_sudoku([    [1, 2, 3, 7, 8, 9, 4, 5, 6],
                                        [4, 5, 6, 1, 2, 3, 7, 8, 9],
                                        [7, 8, 9, 4, 5, 6, 1, 2, 3],
                                        [2, 3, 1, 8, 9, 7, 5, 6, 4],
                                        [5, 6, 4, 2, 3, 1, 8, 9, 7],
                                        [8, 9, 7, 5, 6, 4, 2, 3, 1],
                                        [3, 1, 2, 9, 7, 8, 6, 4, 5],
                                        [6, 4, 5, 3, 1, 2, 9, 7, 8],
                                        [9, 7, 8, 6, 4, 5, 3, 1, 2]  ]) == True # good grid
        print("Test {} passed".format(i))
        i+=1

        assert sudoku.verif_sudoku([    [1, 2, 3, 7, 8, 9, 4, 5, 6],
                                        [4, 5, 6, 1, 2, 3, 7, 8, 9],
                                        [7, 8, 9, 4, 5, 6, 1, 2, 3],
                                        [2, 3, 1, 8, 9, 7, 5, 6, 4],
                                        [5, 6, 4, 2, 3, 1, 8, 9, 7],
                                        [8, 9, 7, 5, 6, 4, 2, 3, 1],
                                        [3, 1, 2, 9, 7, 8, 6, 4, 5],
                                        [6, 4, 5, 3, 1, 2, 9, 7, 8],
                                        [9, 7, 8, 6, 4, 5, 3, 1, 1]  ]) == False # wrong grid
        print("Test {} passed".format(i))
        i+=1
        
        assert sudoku.verif_sudoku([]) == False          # if the list is empty 
        print("Test {} passed".format(i))
        i+=1
        assert sudoku.verif_sudoku(2) == False           # if not a list
        print("Test {} passed".format(i))
        print("OK")
    except AssertionError :
        print("Test {} not passed".format(i))
        print("KO")