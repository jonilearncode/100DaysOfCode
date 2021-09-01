from board import Board

class Bot(Board):
    """Creates the Bot paddle."""
     
    def __init__(self, pos, color, screen_size, vel_y):
        super().__init__(pos, color, screen_size, vel_y)
        
    def alive(self, ball_vel_vector):
        if ball_vel_vector[1] > 0:
            self.move_up()
        elif ball_vel_vector[1] < 0:
            self.move_down()
            
        