class Restaurant():
    """Create a Restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    """Create a method"""
    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type)
    """Create a print method"""
    def open_restaurant():
        print('This restaurant is open.')

#a=Restaurant()
a_restaurant=Restaurant('a_res','beijing')
# ~ print('a argv:'+a_restaurant.restaurant_name)
# ~ print('b argv:'+a_restaurant.cuisine_type)
# ~ print('\n')
# ~ a_restaurant.describe_restaurant()
# ~ a_restaurant.describe_restaurant()
b_restaurant=Restaurant('b_res','tianjin')
c_restaurant=Restaurant('c_res','hebei')
a_restaurant.describe_restaurant()
b_restaurant.describe_restaurant()
c_restaurant.describe_restaurant()
