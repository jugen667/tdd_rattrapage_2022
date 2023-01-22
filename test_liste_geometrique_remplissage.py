import liste_geometrique_remplissage
def test_isGeometric_fill():
    i = 1
    try :
        assert liste_geometrique_remplissage.isGeometric_fill([3, 5, 7, 9], 3) == False
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique_remplissage.isGeometric_fill([], 3) == False          # if the list is empty 
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique_remplissage.isGeometric_fill(2, 3) == False           # if not a list
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique_remplissage.isGeometric_fill([2, 4, 8], 3) == (True,  [2, 4, 8, 16, 64, 256])
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique_remplissage.isGeometric_fill([2, 4, 8], []) == (True,  None)
        print("Test {} passed".format(i))
        print("OK")
    except AssertionError :
        print("Test {} not passed".format(i))
        print("KO")

test_isGeometric_fill();