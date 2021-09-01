from board import Board

class Player(Board):
    """Creates the User paddle."""
     
    def __init__(self, pos, color, screen_size, vel_y):
        super().__init__(pos, color, screen_size, vel_y)
       