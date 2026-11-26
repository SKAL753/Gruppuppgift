def print_grid(self) -> None:
    for row in self.grid:
        for cell in row:
            print(cell, end=" ")
        print()
