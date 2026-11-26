from board import Board
import random, ui

SIZE = 9
MINE_COUNT = 16

def create_mine_positions(size: int, number_of_mines: int) -> list[tuple[int, int]]:
    positions = [(i, j) for i in range(size) for j in range(size)]
    mine_positions = random.sample(positions, number_of_mines)
    return mine_positions

def game_sequence(board) -> None:
    while True:
        selected_coordinates = ui.get_input("\nSkriv in två koordinater av formen: 12 | 1 2 | 1,2\n> ", SIZE)
        selected_action = ui.get_input("\nVill du flagga [f] eller avslöja [r]\n> ", SIZE, "action")
        if selected_action == "f":
            board.toggle_flagged(selected_coordinates)
        ui.print_grid(board)

def main() -> None:
    mine_positions = create_mine_positions(SIZE, MINE_COUNT)

    board = Board(SIZE, MINE_COUNT)
    board.add_mines(mine_positions)
    board.count_adjacent_mines()
    ui.print_grid(board)
    game_sequence(board)

if __name__ == "__main__":
    main()