from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_gameover = ("Courier", 36, "normal")
class Scoreboard(Turtle):
    
    def __init__(self, level):
        """Handles the static GUI of the Level game."""
        super().__init__()
        self.font = FONT
        self.font_gameover = FONT_gameover
        self.level = level
        self.middle_field_dots = []
        self.gui = Turtle()
        self.gui.ht()
        self.gui.pu()
        self.gui.speed('fastest')
        self.gui.color('black')
        self.gui.goto(0, 250)
            
    def draw_score_board(self, level):
        self.gui.write(f'LEVEL {level}', False, align="center", font=self.font)
    
    def draw_gameover(self):
        self.gui.goto(0, 0)
        self.gui.write(f'GAME OVER', False, align="center", font=self.font_gameover)

