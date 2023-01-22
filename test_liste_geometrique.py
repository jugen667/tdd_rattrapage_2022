import liste_geometrique
def test_isGeometric():
    i = 1
    try :
        assert liste_geometrique.isGeometric([3, 5, 7, 9]) == False
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique.isGeometric([]) == False          # if the list is empty 
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique.isGeometric(2) == False           # if not a list
        print("Test {} passed".format(i))
        i+=1
        assert liste_geometrique.isGeometric([2, 4, 8]) == True    # if a number is negative
        print("Test {} passed".format(i))
        print("OK")
    except AssertionError :
        print("Test {} not passed".format(i))
        print("KO")

test_isGeometric();