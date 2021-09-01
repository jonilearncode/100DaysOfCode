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
        self.is_ball_out_bot_side = False
        self.is_ball_out_player_side = False
    
    def move(self, player_position, bot_position):
       # Get current position and update speed vector if needed
       new_pos = (self.ball.position()[0], self.ball.position()[1])
       
       # Collisions
       if self.detect_collision_with_pos(player_position, bot_position):
           self.set_speed((-self.speed[0], self.speed[1]))
       
       # General movement
       if not self.is_ball_out_player_side and new_pos[0] < -self.screen_size[0] + COLLISION_GAP:
        #    self.set_speed((-self.speed[0], self.speed[1]))
        #    new_pos = (-self.screen_size[0] + COLLISION_GAP, new_pos[1])
           self.set_is_ball_out_player_side(True)
           print("Ball() - Ball get out on the player side!")

       elif not self.is_ball_out_bot_side and new_pos[0] > self.screen_size[0] - COLLISION_GAP:
        #    self.set_speed((-self.speed[0], self.speed[1]))
        #    new_pos = (self.screen_size[0] - COLLISION_GAP, new_pos[1])
           self.set_is_ball_out_bot_side(True)
           print("Ball() - Ball get out on the bot side!")
           
       elif new_pos[1] < -self.screen_size[1] + COLLISION_GAP:
           self.set_speed((self.speed[0], -self.speed[1]))
           new_pos = (new_pos[0], -self.screen_size[1] + COLLISION_GAP)

       elif new_pos[1] > self.screen_size[1] - COLLISION_GAP:
           self.set_speed((self.speed[0], -self.speed[1]))
           new_pos = (new_pos[0], self.screen_size[1] - COLLISION_GAP)
       
        # Update position with speed vector
       new_pos = (new_pos[0] + self.speed[0], new_pos[1] + self.speed[1])
       
       if self.is_ball_out_player_side or self.is_ball_out_bot_side:
           # stop moving
           new_pos = (self.ball.position()[0], self.ball.position()[1])
       self.ball.goto(new_pos)
       
    def set_speed(self, new_speed):
        self.speed = new_speed
    
    def get_speed(self):
        return self.speed
        
    def detect_collision_with_pos(self, target_pos_player, target_pos_bot):
        if self.ball.distance(target_pos_player) < BOARD_COLLISION_GAP:
            print("DEBUG: Ball collided with Player! At position: ", target_pos_player)
            return True
        elif self.ball.distance(target_pos_bot) < BOARD_COLLISION_GAP:
            print("DEBUG: Ball collided with Bot! At position: ", target_pos_bot)
            return True
            
    def set_is_ball_out_player_side(self, boolean):
        self.is_ball_out_player_side = boolean
    
    def set_is_ball_out_bot_side(self, boolean):
        self.is_ball_out_bot_side = boolean   
    
    def reset_ball(self):
        self.ball.goto(0,0)
        self.set_is_ball_out_bot_side(False)
        self.set_is_ball_out_player_side(False)
        self.set_speed((-self.speed[0], -self.speed[1])) # Invert last velocity vector