class Animal:
    
    def __init__(self, age, weight, owner):
        self.age = age
        self.weight = weight 
        self.owner = owner
        owner.addAnimal(self)
        
    def __str__(self):
        return f"Animal ({self.age} years old) owned by {self.owner}"
    
    def eat(self):
        print("I eat")
        

class Cat(Animal):
    
    def __init__(self, name, age, weight, owner):
        Animal.__init__(age, weight, owner)
        self.name = name
        
    def __str__(self):
        return f"{self.name}"
        
    def scream(self):
        print("AHHH")
        

class Dog(Animal):
    
    def __init__(self, age, weight, owner):
        Animal.__init__(age, weight, owner)
        
    def __str__(self):
        return f"Dog ({self.age} years old) owned by {self.owner}"

    def digBones(self):
        print("I dig")
        
        
class Person:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        
    def __str__(self):
        return f"{self.name}"
        
    def addAnimal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        else:
            raise Exception(f"{animal} is already owned by f{self.name}")
    
        
    def pet(self):
        print("I pet")    