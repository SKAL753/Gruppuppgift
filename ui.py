def print_grid(board) -> None:
    for row in board.grid:
        for cell in row:
            print(cell, end=" ")
        print()
