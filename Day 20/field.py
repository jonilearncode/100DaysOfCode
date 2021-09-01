from turtle import Turtle

MIDDLE_FIELD_DOT_SIZE = (20,20)


class Field(Turtle):
    """Handles the static GUI of the Pong game."""
    def __init__(self):
        super().__init__()
        self.middle_field_dots = []
        self.score = Turtle()
        self.score.ht()
        self.score.pu()
        self.score.speed('fastest')
        self.score.color('white')
        self.score.goto(0, 250)
    
    def draw_middle_field(self, center_pos, screen_size_y):
        num_of_dots = int(screen_size_y / (MIDDLE_FIELD_DOT_SIZE[1]))
        for i in range(0,num_of_dots):
            self.middle_field_dots.append(Turtle())
            self.middle_field_dots[i].ht()
            self.middle_field_dots[i].pu()
            self.middle_field_dots[i].speed('fastest')
            self.middle_field_dots[i].color('white')
            self.middle_field_dots[i].shape('square')
            self.middle_field_dots[i].goto(center_pos[0], int(screen_size_y - MIDDLE_FIELD_DOT_SIZE[1] * i * 2))
            self.middle_field_dots[i].st()
        # Grant space for the SCORE label
        self.middle_field_dots[0].ht()
        self.middle_field_dots[1].ht()
        self.middle_field_dots[2].ht()
    
    def draw_score_board(self, score):
        self.score.write(f'{score[0]} SCORE {score[1]}', False, align="center", font=("Arial", 24, "bold"))

