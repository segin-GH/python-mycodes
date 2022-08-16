from main import sqr



def main():
    test_sqrFunction()



def test_sqrFunction():
    # assert sqr(2) == 4;
    # assert sqr(3) == 9;
    # assert sqr(-2) == 4;
    # assert sqr(-3) == 9;
    # assert sqr(0) == 0;

# test 0
    try:
        assert sqr(2) == 4;
    except AssertionError:
        print(" test_sqrFunction() : Test 0 is Failed")
# test 1
    try:
        assert sqr(3) == 9;
    except AssertionError:
        print(" test_sqrFunction() : Test 1 is Failed")
#test 2
    try:
        assert sqr(-2) == 4;
    except AssertionError:
        print(" test_sqrFunction() : Test 2 is Failed")
#test 3
    try:
        assert sqr(-3) == 9;
    except AssertionError:
        print(" test_sqrFunction() : Test 3 is Failed")
#test 4
    try:
        assert sqr(0) == 0;
    except AssertionError:
        print(" test_sqrFunction() : Test 4 is Failed")



    # if sqr(2) != 4:
    #     print(" test_sqrFunction() : Test 0 is Failed")

    # if sqr(3) != 9:
    #     print(" test_sqrFunction() : Test 1 is Failed")



if __name__ == "__main__":
    main()

