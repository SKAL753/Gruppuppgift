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

    def create_mine_positions(self) -> list[tuple[int, int]]:
        positions = [(i, j) for i in range(self.size) for j in range(self.size)]
        mine_positions = random.sample(positions, self.number_of_mines)
        return mine_positions
    
    def add_mines(self) -> None:
        mine_positions = self.create_mine_positions()
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
    
    def toggle_flagged(self, coordinates):
        y, x = coordinates
        current_cell = self.grid[y][x]
        if not (current_cell.is_revealed):
            current_cell.is_flagged = not current_cell.is_flagged

    def reveal_cell(self, coordinates):
        y, x = coordinates
        current_cell = self.grid[y][x]
        if current_cell.is_flagged:
            return
        

    def cell_reveal_algoritm(self, coordinates):
        row, column = coordinates
        current_cell = self.grid[row][column]
        if current_cell.is_revealed:
            return

        self.reveal_cell(coordinates)

        if current_cell.neighboring_mines > 0:
                return
        
        for row_offset in (-1,0,1):
            for column_offset in (-1,0,1):

                if row_offset == 0 and column_offset == 0:
                    continue

                if (0 <= row + row_offset < self.size and 0 <= column + column_offset < self.size):
                    self.cell_reveal_algoritm((row + row_offset, column + column_offset))           
