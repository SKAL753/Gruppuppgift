from board import Board
import random, ui

SIZE = 9
MINE_COUNT = 16


class Game:
    def __init__(self):
        self.board = Board(SIZE, MINE_COUNT)
        self.is_running = True

    def game_sequence(self) -> None:
        while True:
            selected_coordinates = ui.get_input("\nSkriv in två koordinater av formen: 12 | 1 2 | 1,2\n> ", SIZE)
            selected_action = ui.get_input("\nVill du flagga [f] eller avslöja [r]\n> ", SIZE, "action")
            if selected_action == "f":
                self.board.toggle_flagged(selected_coordinates)
            elif selected_action == "r":
                pass
            ui.print_grid(self.board)

    def setup_board(self):
        self.board.add_mines()

    def start(self) -> None:
        self.setup_board()
        ui.print_grid(self.board)
        self.game_sequence()