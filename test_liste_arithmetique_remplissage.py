import liste_arithmetic_remplissage
def test_isArithmetic_fill():
    i = 1
    try :
        assert liste_arithmetic_remplissage.isArithmetic_fill([3, 5, 7, 9], 3) == (True, [3, 5, 7, 9, 11, 13, 15])
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic_remplissage.isArithmetic_fill([], 3) == False          # if the list is empty 
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic_remplissage.isArithmetic_fill(2, 3) == False           # if not a list
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic_remplissage.isArithmetic_fill([2, 4, 10, 78], 3) == False  
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic_remplissage.isArithmetic_fill([2, 4, 6], []) == (True, None)  
        print("Test {} passed".format(i))
        print("OK")
    except AssertionError :
        print("Test {} not passed".format(i))
        print("KO")

test_isArithmetic_fill();