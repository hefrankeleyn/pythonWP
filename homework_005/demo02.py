class User():
    """Create a User class."""
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(self.first_name+'\t'+self.last_name)
    def greet_user(self): 
        print('Good momning,'+self.first_name.title()+' '+self.last_name.title())

#Create user
a_user=User('a','Acia')
b_user=User('b','Haha')
a_user.greet_user()
b_user.greet_user()
