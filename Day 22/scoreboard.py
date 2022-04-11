from turtle import Turtle, mode

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("black")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        try:
            self.load_highscore()
        except Exception as e:
            print('Creating new highscore.txt file.')

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.save_highscore()
            self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def save_highscore(self):
        with open('highscore.txt', mode='w') as file:
            file.write(str(self.highscore))
    
    def load_highscore(self):
        with open('highscore.txt', mode='r') as file:
            self.highscore = int(file.read()) 
