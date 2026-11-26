class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = True
        self.is_flagged = False
        self.neighboring_mines = 0
    def __str__(self):
        if self.is_mine:
            return "[*]"
        if self.is_revealed:
            if self.neighboring_mines > 0:
                return f"[{self.neighboring_mines}]"
        return "[ ]"
