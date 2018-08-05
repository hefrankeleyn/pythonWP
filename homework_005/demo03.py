class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def open_restaurant(self):
        print('welcome to here.')
    def describe_restaurant(self):
        print(self.restaurant_name+'\t'+self.cuisine_type+'\t'+
              str(self.number_served))
    def set_number_served(self,number_served):
        self.number_served=number_served
    def increment_number_served(self,number_served):
        self.number_served+=number_served

a_restaurant=Restaurant('aa','bb',23)
b_restaurant=Restaurant('aa','bb')
a_restaurant.describe_restaurant()
b_restaurant.describe_restaurant()
b_restaurant.set_number_served(8)
b_restaurant.describe_restaurant()
b_restaurant.increment_number_served(12)
b_restaurant.describe_restaurant()
