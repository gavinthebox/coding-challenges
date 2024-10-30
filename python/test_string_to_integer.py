from string_to_integer import string_to_integer

def test_string_to_integer():
    # Basic cases
    assert string_to_integer("123") == 123, "Test case 1 failed"
    assert string_to_integer("0") == 0, "Test case 2 failed"
    
    # Edge cases
    assert string_to_integer("000123") == 123, "Test case 3 failed"  # leading zeros
    assert string_to_integer("2147483647") == 2147483647, "Test case 4 failed"  # max 32-bit int



    print("All tests passed!")

if __name__ == "__main__":
    test_string_to_integer()