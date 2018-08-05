class User():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def user_login(self):
        print('Welcome to China,'+self.username.title()+' '
               +self.password.title())
    
class Admin(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.privileges=Privileges()
    


class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('The admin have those privilege:')
        for privilege in self.privileges:
            print('\t'+privilege)

admin=Admin('xiaoming','123')
admin.privileges.show_privileges()
            
