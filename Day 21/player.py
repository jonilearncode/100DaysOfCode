from turtle import Turtle

class Player(Turtle):
    """Creates the Player."""
     
    def __init__(self, pos, screen_size, velocity_y):
        super().__init__()
        self.screen_size = screen_size
        self.velocity_y = velocity_y
        self.player = Turtle()
        self.player.ht()
        self.player.pu()
        self.player.speed('fastest')
        self.player.shape('turtle')
        self.player.left(90)
        self.player.goto(pos)
        self.player.st()
    
    def move_up(self):
        if self.player.position()[1] < self.screen_size[1]:
            self.player.goto(self.player.position()[0], self.player.position()[1] + self.velocity_y)
        else:
            self.player.goto(self.player.position()[0], self.screen_size[1] - 5)
            
    
    def get_position(self):
        return self.player.position()
        
