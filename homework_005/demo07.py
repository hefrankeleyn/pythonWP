class Car():
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def show_descrip(self):
        print(self.make+'\t'+self.model)

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print('This battery is '+self.battery_size)
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        else:
            range=0
        return range
class ElectricCar(Car):
    def __init__(self,make,model):
        super().__init__(make,model)
        self.battery=Battery()
electricCar=ElectricCar('Msk','apple')
range=electricCar.battery.get_range()
print(range)
electricCar.battery.upgrade_battery()
print(electricCar.battery.get_range())
