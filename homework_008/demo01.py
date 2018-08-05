class City_Country():
    def __init__(self,city,country,population=0):
        self.city=city
        self.country=country
        self.population=population
    def show_city_and_country(self):
        city_and_country=self.city.title()+','+self.country.title()+' - population '+str(self.population)
        return city_and_country
