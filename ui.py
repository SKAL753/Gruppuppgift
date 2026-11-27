def print_grid(board) -> None:
    for row in board.grid:
        for cell in row:
            print(cell, end=" ")
        print()

def get_input(line: str, size: int, input_type = None) -> tuple[int]:
    while True:
        user_input = input(line).strip().lower().replace(" ", "").replace(",", "")
        if input_type == "action":
            if verify_input_action(user_input):
                return user_input
        if verify_input_coordinates(user_input, size):
            return tuple(map(int, user_input))

def verify_input_coordinates(user_input: str, size: int) -> bool:
    if user_input.isalnum():
        if len(user_input) == 2:
            if (0 <= int(user_input[0]) < size and 0 <= int(user_input[1]) < size):
                return True
            
def verify_input_action(user_input: str) -> bool:
    if user_input == "f" or user_input == "r":
        return True
