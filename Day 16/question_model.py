from data import question_data
import random

class DataBase:
    """Models the questions data set for a quiz game."""
    def __init__(self):
        self.questions = question_data.copy()
        
    def get_db(self):
        """Returns a list with dictionary where keys are questions and values their correct answers."""
        return self.questions


class QuestionModel:
    """Models the questions and their correct answers for a quiz game."""
    def __init__(self, dataset):
        """Initialize a question model from desired dictionary with questions and answers."""
        self.dataset = dataset
    
    def get_random_entry(self):
        """Retrieves a random pair key:value from questions data set and updates db."""
        rand_index = random.randint(0, len(self.dataset) - 1)
        entry = self.dataset[rand_index]
        self.dataset.pop(rand_index)
        return entry
    
    def eval_answer(self, entry, answer):
        """Provide a entry entry key/value and get a boolean check between entry.key value and answer."""
        result = entry['answer']
        if result == answer:
            print(f'You got it right!')
            print(f'The correct answer was: {result}')            
            return True
        print(f'You got it wrong.')
        print(f'The correct answer was: {result}')            
        return False
    
    def prompt_question_text(self, entry, numeration):
        """Input a question to user and retrieves his answer."""
        text = entry['text']
        return input(f'Q{numeration}: {text}. (True/False)?:  ')
