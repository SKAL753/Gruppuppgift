from board import Board
import random, ui

SIZE = 9
MINE_COUNT = 16

def create_mine_positions(size: int, number_of_mines: int) -> list[tuple[int, int]]:
    positions = [(i, j) for i in range(size) for j in range(size)]
    mine_positions = random.sample(positions, number_of_mines)
    return mine_positions

def main():
    mine_positions = create_mine_positions(SIZE, MINE_COUNT)

    board = Board(SIZE, MINE_COUNT)
    board.add_mines(mine_positions)
    board.count_adjacent_mines()
    ui.print_grid()

if __name__ == "__main__":
    main()