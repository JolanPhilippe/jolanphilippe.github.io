import copy


class City:
    
    __currentId = 0
    
    def __init__(self, name, num_inhabitant):
        self.__name = name
        self.__num_inhabitant = num_inhabitant
        self.__id = City.__currentId
        City.__currentId += 1 
        self.__country = None
        
    def __str__(self):
        return f"{self.getName()} (with id={self.getId()})"
    
    def __copy__(self):
        return copy.copy(self)
    
    def __deepcopy__(self):
        return copy.deepcopy(self)
    
    def __eq__(self, another_object):
        if isinstance(another_object, City):
            return City.__areTheSameCities(self, another_object)
        else:
            return False
    
    def __areTheSameCities(cityA, cityB):
        if not cityA.getName() == cityB.getName():
            print("name difference")
            return False
        if not cityA.getNumInhab() == cityB.getNumInhab():
            print("inhab difference")
            return False
        if not cityA.getCountry() == cityB.getCountry():
            print("country difference")
            return False
        return True
    
    def getId(self):
        return self.__id 
    
    def getName(self):
        return self.__name
    
    def getNumInhab(self):
        return self.__num_inhabitant
    
    def getCountry(self):
        return self.__country
    
    def isACapitalCity(city):
        return city.__country.__capital == city
    
    def getTheBestCities(cities):
        votes = {} # key: City -> vlue: number of vote
        # First we collect the number of votes for each city
        for city in cities:
            if city.getName() not in votes.keys():
                votes[city.getName()] = 0
            votes[city.getName()] += 1
        # Then we find the city with the max number of votes
        winner = None
        best = 0
        for city in cities:
            if votes[city.getName()] > best:
                best = votes[city.getName()]
                winner = city
        return winner
        

  
class Country:
    
    def __init__(self, name, capital):
        self.__name = name
        self.__capital = capital
        self.__cities = [capital]
        capital.country = self
        
    def getName(self):
        return self.__name

    def getCapital(self):
        return self.__capital
    
    def getCities(self):
        return self.__cities
    
    def __str__(self):
        return f"{self.__name}"
    
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

        
    def setCapital(self, city):
        print(f"The new capital of {self} is {city}")
        self.__capital = city

if __name__ == "__main__":
    nantes = City("Nantes", 332417)
    nantes2 = City("Nantes", 332417)
    paris = City("Paris", 2161000)
    orleans = City("Orleans", 114644)
    france = Country("France", paris)
    cities = [nantes, paris, orleans]
    if nantes == nantes2:
        print("Nantes is Nantes")
    else:
        print("Nantes is not Nantes")
        
    votes = [nantes, orleans, orleans, paris, nantes, nantes]
    bestcity = City.getTheBestCities(votes)
    france.setCapital(bestcity)
