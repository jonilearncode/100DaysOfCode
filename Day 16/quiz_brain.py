class QuizBrain:
    """Models the main logic for the quiz game."""
    def __init__(self, game_attempts):
        """Initializes the game with 0 score and 0 attempts."""
        self.score = 0
        self.attempts = 0
        self.game_attempts = game_attempts
    
    def get_score(self):
        return self.score

    def get_attempts(self):
        return self.attempts
    
    def update_score(self, value):
        self.score += value
        print(f'Your current score is: {self.score}/{self.game_attempts}')
    
    def update_attempts(self, value):
        self.attempts += value
    
    def is_gameover(self):
        if self.attempts > self.game_attempts:
            return True
        return False
