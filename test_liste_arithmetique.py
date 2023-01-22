import liste_arithmetic
def test_isArithmetic():
    i = 1
    try :
        assert liste_arithmetic.isArithmetic([3, 5, 7, 9]) == True
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic.isArithmetic([]) == False          # if the list is empty 
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic.isArithmetic(2) == False           # if not a list
        print("Test {} passed".format(i))
        i+=1
        assert liste_arithmetic.isArithmetic([2, 4, 10, 78]) == False  
        print("Test {} passed".format(i))
        print("OK")
    except AssertionError :
        print("Test {} not passed".format(i))
        print("KO")

test_isArithmetic();