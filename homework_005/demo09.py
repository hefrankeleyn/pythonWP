from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))
    def show_ran_num(self):
        for i in range(10):
            print(randint(1,self.sides))
        print('\n')

die01=Die()
die01.show_ran_num()


die02=Die(10)
die02.show_ran_num()
die03=Die(20)
die03.show_ran_num()
