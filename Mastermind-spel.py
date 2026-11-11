def validate_input(user_input): 
        user_input = user_input.replace(" ", "")
        user_input_lst = list(user_input)
        if len(user_input_lst) == 4:
            for item in user_input_lst:
                if not item.isdigit():
                    return False
                if int(item) > 6 or int(item) < 1:
                    return False
            return True
        return False
        
    

def get_input(line):
    while True:
        user_input = input(line)
        if validate_input(user_input):
            pass

def write_output():
    pass

def test_validate_input():
    print(validate_input("1234"))
    print(validate_input("123 4"))
    print(validate_input("12 34"))
    print(validate_input("1a34"))
    print(validate_input("134"))
    print(validate_input("12345"))

test_validate_input()
