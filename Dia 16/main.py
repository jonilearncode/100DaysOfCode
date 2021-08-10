from question_model import QuestionModel, DataBase
from quiz_brain import QuizBrain
import os

# Globals
os.system("cls")
intro = "Welcome to Q&A with PyClasses! Made by Joao Teixeira 2021."
db =  DataBase().get_db()
question_model = QuestionModel(db)
game_attempts = 4
quiz_game = QuizBrain(game_attempts)

# Main logic
while not quiz_game.is_gameover():
    rand_entry = question_model.get_random_entry()
    answer = question_model.prompt_question_text(rand_entry, quiz_game.get_attempts())
    if question_model.eval_answer(rand_entry, answer):
        quiz_game.update_score(1)
    else:
        quiz_game.update_score(0)
    quiz_game.update_attempts(1)
    print('\n')
