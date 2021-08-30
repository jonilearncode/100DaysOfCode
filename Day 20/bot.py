from board import Board

class Bot(Board):
    """Creates the Bot paddle."""
     
    def __init__(self, pos, color, screen_size):
        super().__init__(pos, color, screen_size)
        