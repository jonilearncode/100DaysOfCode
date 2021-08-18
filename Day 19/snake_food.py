import turtle

class SnakeFood():
    
    def __init__(self, pos):
        self.eaten_food_amount = 0
        self.food = turtle.Turtle()
        self.food.ht()
        self.food.pu()
        self.food.color('green')
        self.food.shape('circle')
        self.food.goto(pos)
        self.food.st()
        
    def delete_food(self, food_pos):
        if self.food.position()[0] == food_pos[0] and self.food.position()[1] == food_pos[1]:
            self.eaten_food_amount += 1
            self.food.ht()
        else:
            print(f'ERROR - class SnakeFood, delete_food() can\'t delete food at pos = {food_pos}.')
    
    def create_food(self, food_pos):
        self.food.goto(food_pos)
        self.food.st()
        
    def get_score(self):
        return self.eaten_food_amount
    
    def has_food(self):
        if self.food.isvisible():   
            return True
        else:
            return False
        
    def get_position(self):
        return self.food.position()