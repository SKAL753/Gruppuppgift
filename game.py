from board import Board
import ui

SIZE = 9
MINE_COUNT = 16


class Game:
    def __init__(self):
        self.board = Board(SIZE, MINE_COUNT)
        self.is_running = True

    def game_sequence(self) -> bool:
        while self.is_running:
            selected_coordinates = ui.get_input("\nSkriv in två koordinater av formen: 12 | 1 2 | 1,2\n> ", SIZE)
            selected_action = ui.get_input("\nVill du flagga [f] eller avslöja [r]\n> ", SIZE, "action")
            if selected_action == "f":
                self.board.toggle_flagged(selected_coordinates)
            elif selected_action == "r":
                self.reveal_selected_cell(selected_coordinates)
            ui.print_grid(self.board)
            
            if self.check_win():
                return True
        return False

    def reveal_selected_cell(self, coordinates: tuple[int, int]) -> None:
        row, column = coordinates
        cell = self.board.grid[row][column]

        if cell.is_flagged or cell.is_revealed:
            return

        if cell.is_mine:
            self.board.reveal_cell(coordinates)
            self.is_running = False
            return

        self.board.cell_reveal_algorithm(coordinates)

    def setup_board(self) -> None:
        self.board.add_mines()
        self.board.count_adjacent_mines()

    def start(self) -> None:
        self.setup_board()
        ui.print_grid(self.board)
        if self.game_sequence():
            self.end_game_win()
        else:
            self.end_game_loss()


    def check_win(self) -> bool:
        for row in self.board.grid:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def end_game_win(self) -> None:
        self.is_running = False
        ui.print_win()

    def end_game_loss(self) -> None:
        self.is_running = False
        ui.print_loss()