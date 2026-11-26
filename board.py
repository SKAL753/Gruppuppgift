import random
from cell import Cell


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
    
    def count_adjacent_mines(self):
        for row in range(self.size):
            for column in range(self.size):
                current_cell = self.grid[row][column]

                if current_cell.is_mine:
                    continue

                for row_offset in (-1,0,1):
                    for column_offset in (-1,0,1):

                        if row_offset == 0 and column_offset == 0:
                            continue

                        if not (0 <= row + row_offset < self.size and 0 <= column + column_offset < self.size):
                            continue 

                        if self.grid[row + row_offset][column + column_offset].is_mine:
                            current_cell.neighboring_mines += 1



