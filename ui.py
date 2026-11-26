def print_grid(board) -> None:
    for row in board.grid:
        for cell in row:
            print(cell, end=" ")
        print()

def get_input(line, size):
    user_input = input(line).strip().replace(" ", "").replace(",", "")
    print(user_input)
    if verify_input(user_input, size):
        print("Blev godkänd")
        return user_input

def verify_input(user_input, size):
    if user_input.isalnum():
        if len(user_input) == 2:
            if (0 <= int(user_input[0]) < size and 0 <= int(user_input[1]) < size):
                return True

get_input("Skriv något: ", 9)