from turtle import Turtle

BALL_SPEED = (4,4)
COLLISION_GAP = 20
BOARD_COLLISION_GAP = 40

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
        # self.ball.shapesize(2, 2, 1)
        self.ball.goto(pos)
        self.ball.st()
        self.speed = BALL_SPEED
    
    def move(self, board_target_position):
        # Get current position and update speed vector if needed
       new_pos = (self.ball.position()[0], self.ball.position()[1])
       
       # Collisions
       if self.detect_collision_with_pos(board_target_position):
           self.set_speed((-self.speed[0], self.speed[1]))
       
       # General movement
       if new_pos[0] < -self.screen_size[0] + COLLISION_GAP:
           self.set_speed((-self.speed[0], self.speed[1]))
           new_pos = (-self.screen_size[0] + COLLISION_GAP, new_pos[1])
           
       elif new_pos[0] > self.screen_size[0] - COLLISION_GAP:
           self.set_speed((-self.speed[0], self.speed[1]))
           new_pos = (self.screen_size[0] - COLLISION_GAP, new_pos[1])
           
       elif new_pos[1] < -self.screen_size[1] + COLLISION_GAP:
           self.set_speed((self.speed[0], -self.speed[1]))
           new_pos = (new_pos[0], -self.screen_size[1] + COLLISION_GAP)

       elif new_pos[1] > self.screen_size[1] - COLLISION_GAP:
           self.set_speed((self.speed[0], -self.speed[1]))
           new_pos = (new_pos[0], self.screen_size[1] - COLLISION_GAP)
        # Update position with speed vector
       new_pos = (new_pos[0] + self.speed[0], new_pos[1] + self.speed[1])
       self.ball.goto(new_pos)
       
    def set_speed(self, new_speed):
        self.speed = new_speed
        
    def detect_collision_with_pos(self, target_pos):
        if self.ball.distance(target_pos) < BOARD_COLLISION_GAP:
            print("DEBUG: Ball collided with a Board! At position: ", target_pos)
            return True
            
        