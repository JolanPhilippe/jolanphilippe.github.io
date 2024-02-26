class City:
    
    def __init__(self, name, num_inhabitant):
        self.name = name
        self.num_inhabitant = num_inhabitant
        self.country = None
        
    def __str__(self):
        return f"{self.name}"
        
    def isACapitalCity(city):
        return city.country.capital == city

class Country:
    
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        self.cities = [capital]
        capital.country = self
        
    def __str__(self):
        return f"{self.name}"
    
    def num_inhabitants(self):
        result = 0
        for city in self.cities:
            result += city.num_inhabitant
        return result
    
    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            city.country = self
        else:
            raise Exception(f"{city} is already a city of {self}")
    
    def rm_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            city.country = None
        else:
            raise Exception(f"{city} is not a city of {self}")
        

if __name__ == "__main__":
    nantes = City("Nantes", 332417)
    paris = City("Paris", 2161000)
    orleans = City("Orleans", 114644)
    france = Country("France", paris)
    cities = [nantes, paris, orleans]
    for city in cities:
        try:
            france.add_city(city)
        except Exception as e:
            print(e)
    for city in cities:
        if City.isACapitalCity(city):
            print(f"{city} is a capital city")  
        else:
            print(f"{city} is not a capital city")  
    
    