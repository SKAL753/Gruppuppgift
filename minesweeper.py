import random

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
    
def create_cells(size: int) -> list[list[Cell]]:
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(Cell())
        grid.append(row)
    return grid

def create_mine_positions(size: int, number_of_mines: int) -> list[tuple[int, int]]:
    positions = [(i, j) for i in range(size) for j in range(size)]
    mine_positions = random.sample(positions, number_of_mines)
    return mine_positions

def add_mines(grid: list[list[Cell]], mine_positions: list[tuple[int, int]]) -> None:
    for row, col in mine_positions:
        grid[row][col].is_mine = True
    
def print_grid(grid:list[list[Cell]]) -> None:
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

mine_positions = create_mine_positions(9, 16)
grid = create_cells(9)
add_mines(grid, mine_positions)
print_grid(grid)
    

