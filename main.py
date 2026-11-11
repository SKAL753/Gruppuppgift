def validate_input(user_input): 
        user_input = user_input.replace(" ", "")
        if user_input.isdigit():
            if len(user_input) == 4:
                return True
        else: 
            return False
    

def get_input(line):
    while True:
        user_input = input(line)
        if validate_input(user_input):
            pass

def write_output():
    pass

