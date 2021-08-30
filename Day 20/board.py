from turtle import Turtle

VELOCITY_Y = 10

class Board(Turtle):
    """Creates the paddles for the players."""
     
    def __init__(self, pos, color, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.paddle = Turtle()
        self.paddle.ht()
        self.paddle.pu()
        self.paddle.speed('fastest')
        self.paddle.color(color)
        self.paddle.shape('square')
        self.paddle.shapesize(2, 1, 1)
        self.paddle.goto(pos)
        self.paddle.st()
    
    def move_up(self):
        if self.paddle.position()[1] < self.screen_size[1]:
            self.paddle.goto(self.paddle.position()[0], self.paddle.position()[1] + VELOCITY_Y)
        else:
            self.paddle.goto(self.paddle.position()[0], self.screen_size[1] - 5)
            
    
    def move_down(self):
        if self.paddle.position()[1] > -self.screen_size[1]:
            self.paddle.goto(self.paddle.position()[0], self.paddle.position()[1] - VELOCITY_Y)
        else:
            self.paddle.goto(self.paddle.position()[0], -self.screen_size[1] + 5)
    
    
    