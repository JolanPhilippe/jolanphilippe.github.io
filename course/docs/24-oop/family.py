class Family:
    
    def __init__(self, name):
        self.name = name
        self.members = []
        
    def addMembers(self, member):
        if member in self.members:
            raise Exception(f"{member} is already a member of {self.name}")
        else:
            self.members.add(member)
    
class Person:
    
    def __init__(self, firstname, family, age, height, color, gender):
        self.fistname = firstname
        self.family = family
        family.addMembers(self)
        self.age = age
        self.height = height
        self.favoriteColor = color
        self.gender = gender
    
class Gender:
    
    def __init__(self):
        pass
    
class Male(Gender):
    
    def __init__(self):
        pass
    
class Female(Gender):
    
    def __init__(self):
        pass
    
class NonBinary(Gender):
    
    def __init__(self):
        pass
    
class OtherGender(Gender):
    
    def __init__(self):
        pass
    
class Animal:
    
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie
        
    def eat(self, food):
        print(f"{self.name} eats {food}")
    
    def scream(self):
        pass
    
class Cat(Animal):
    
    def __init__(self):
        pass
    
    def scream(self):
        print("Miaou")
    
class Rabbit(Animal):
    
    def __init__(self):
        pass
    
    def scream(self):
        print("Croucr")
    
class Dog(Animal):
    
    def __init__(self):
        pass
    
    def scream(self):
        print("Waf")

class Bird(Animal):
    
    def __init__(self):
        pass
    
    def scream(self):
        print("Piou piou")
    
    