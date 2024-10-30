from valid_parenthesis import valid_parenthesis

def test_valid_parenthesis():
    assert valid_parenthesis("()") == True, "Test case 1 failed"
    assert valid_parenthesis("()[]{}") == True, "Test case 2 failed"
    assert valid_parenthesis("(]") == False, "Test case 3 failed"  
    assert valid_parenthesis("([])") == True, "Test case 4 failed" 
    assert valid_parenthesis("({[}])") == False, "Test case 5 failed"



    print("All tests passed!")

if __name__ == "__main__":
    test_valid_parenthesis()