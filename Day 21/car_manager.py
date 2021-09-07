from turtle import Turtle, screensize
import random

NUMBER_OF_LANES = 10
SPACE_BETWEEN_LANES = 50
CARS_LANES_OFFSET_Y = 80
CARS_START_AT_X_PERCENTAGE = 0.98

class CarManager(Turtle):
    def __init__(self, screen_size, cars_colors, initial_vel):
        super().__init__()
        self.screen_size = screen_size
        self.cars = []
        self.colors = cars_colors
        self.vel = initial_vel
        self.initial_pos = []
        self.cars_speeds_x = []
        self.marked_for_delete = False
    
    def delete(self):
        while len(self.cars) > 0:
            self.cars[0].ht()
            self.cars.pop(0)
            
    def initialize_cars(self):
        num_of_slots = int((self.screen_size[1] / 2) / NUMBER_OF_LANES)
        for i in range(0, num_of_slots):
            self.initial_pos.append((self.screen_size[0] * CARS_START_AT_X_PERCENTAGE, ((-self.screen_size[1]) + CARS_LANES_OFFSET_Y + i * SPACE_BETWEEN_LANES)))
        
        for i in range(0, NUMBER_OF_LANES):
            self.car = Turtle()
            self.car.ht()
            self.car.pu()
            self.car.speed('fastest')
            self.car.color(self.colors[random.randint(0, len(self.colors) - 1)])
            self.car.shape('square')
            self.car.shapesize(1, 2, 1)
            self.car.goto(self.initial_pos[i])
            self.car.st()
            self.cars.append(self.car)
            self.cars_speeds_x.append(random.uniform(self.vel * 0.65, self.vel))
        
    
    def move(self):
        for i in range(len(self.cars)):
            self.cars[i].goto(self.cars[i].position()[0] - self.cars_speeds_x[i], self.cars[i].position()[1])
    
    def check_if_wave_is_on_initial(self):
        """Evaluates if a car in this wave have ran the screen to the predetermined x_pos. If so, returns True."""
        for car in self.cars:
            if car.position()[0] < self.screen_size[0] * 0.45:
                return True
        return False
    
    def check_if_wave_is_finished(self):
        """Evaluates if a car in this wave have ran the screen. If so, returns True."""
        for car in self.cars:
            if car.position()[0] < -self.screen_size[0] * 0.5:
                return True
        return False
    
    def to_del(self):
        if self.marked_for_delete == True:
            return True
        return False