from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        """init random_walk num"""
        self.num_points = num_points
        
        #all walk_num begin (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """show all walk_num point"""
        while len(self.x_values) <self.num_points:
            #direction
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_distance*x_distance
