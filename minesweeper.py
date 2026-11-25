import random

SIZE = 9
MINE_COUNT = 16

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighboring_mines = 0
    def __str__(self):
        if self.is_mine:
            return "[*]"
        return "[ ]"

class Board:
    def __init__(self, size: int, number_of_mines: int) -> None:
        self.size = size
        self.number_of_mines = number_of_mines
        self.grid = self.create_cells(size)
    
    def create_cells(self, size: int) -> list[list[Cell]]:
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell())
            grid.append(row)
        return grid
    
    def add_mines(self, mine_positions: list[tuple[int, int]]) -> None:
        for row, col in mine_positions:
            self.grid[row][col].is_mine = True
    
    def count_adjacent_mines():
        pass

    def print_grid(self) -> None:
        for row in self.grid:
            for cell in row:
                print(cell, end=" ")
            print()

def create_mine_positions(size: int, number_of_mines: int) -> list[tuple[int, int]]:
    positions = [(i, j) for i in range(size) for j in range(size)]
    mine_positions = random.sample(positions, number_of_mines)
    return mine_positions


mine_positions = create_mine_positions(SIZE, MINE_COUNT)

board = Board(SIZE, MINE_COUNT)
board.add_mines(mine_positions)
board.print_grid()
    

