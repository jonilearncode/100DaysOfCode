from turtle import Turtle

class Player(Turtle):
    """Creates the Player."""
     
    def __init__(self, pos, screen_size, velocity_y):
        super().__init__()
        self.screen_size = screen_size
        self.velocity_y = velocity_y
        self.starting_position = pos
        self.player = Turtle()
        self.player.ht()
        self.player.pu()
        self.player.speed('fastest')
        self.player.shape('turtle')
        self.player.left(90)
        self.player.goto(self.starting_position)
        self.player.st()
    
    def move_up(self):
        if self.player.position()[1] < self.screen_size[1]:
            self.player.goto(self.player.position()[0], self.player.position()[1] + self.velocity_y)
        else:
            self.player.goto(self.player.position()[0], self.screen_size[1] - 5)
    
    def move_down(self):
        if self.player.position()[1] > -self.screen_size[1]:
            self.player.goto(self.player.position()[0], self.player.position()[1] - self.velocity_y)
        else:
            self.player.goto(self.player.position()[0], -self.screen_size[1] + 5)
            
    def get_position(self):
        return self.player.position()
        
    def has_reach_finish_line(self, finish_line):
        if self.player.distance(finish_line) < 10:
            return True
        else:
            return False
    
    def is_colliding(self, car):
        # print(f'[DEBUG] Player() pos = {self.player.position()} --- car pos = {car.position()}')
        if self.player.distance(car.position()) < 25:
            return True
        return False
    
    def reset_pos(self):
        self.player.ht()
        self.player.goto(self.starting_position)
        self.player.st()