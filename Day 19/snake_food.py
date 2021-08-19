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
        self.food.speed('fastest')
        
    def delete_food(self):
        self.eaten_food_amount += 1
        self.food.ht()
    
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