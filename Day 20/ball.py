from turtle import Turtle

class Ball(Turtle):
    """Creates the Pong ball."""
     
    def __init__(self, pos, color, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.ball = Turtle()
        self.ball.ht()
        self.ball.pu()
        self.ball.speed('fastest')
        self.ball.color(color)
        self.ball.shape('circle')
        self.ball.shapesize(2, 2, 1)
        self.ball.goto(pos)
        self.ball.st()