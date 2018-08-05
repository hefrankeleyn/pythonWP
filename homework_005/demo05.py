class Restaurant():
    def __init__(self,flavors):
        self.flavors=flavors
    def show_flavors(self):
        print('This is '+self.flavors)


class IceCreamStand(Restaurant):
    def __init__(self,flavors):
        super().__init__(flavors)

ice=IceCreamStand('apple ice')
ice.show_flavors()
