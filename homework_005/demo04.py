class User():
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts
    def describe_user(self):
        print(self.first_name+'\t'+self.last_name)
    def greet_user():
        print('Welcome to China,'+self.first_name.title()
               +self.last_name.title())
    def increment_login_attempts(self):
        self.login_attempts+=1
    def rest_login_attempts(self):
        self.login_attempts=0

user=User('xiao','ming',1)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print('login_attempts:'+str(user.login_attempts))
user.rest_login_attempts()
print('login_attempts:'+str(user.login_attempts))
        
