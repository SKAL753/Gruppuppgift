class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighboring_mines = 0
    def __str__(self):
        if self.is_flagged:
            return "[⚑]"
        if self.is_mine:
            return "[*]"
        if self.is_revealed:
            if self.neighboring_mines > 0:
                return f"[{self.neighboring_mines}]"
            else:
                return "[-]"
        return "[ ]"
