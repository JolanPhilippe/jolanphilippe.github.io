import math

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cartesianDistance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    
    
class City(Point):
    
    def __init__(self, x, y, name, inhabitant):
        Point.__init__(self, x, y)     
        self.name = name
        self.num_inhabitant = inhabitant
    
    def __str__(self):
        return f"{self.name} ({self.x}, {self.y}) [{self.num_inhabitant}]"

    def addInhabitants(self, n):
        if n >= 0:        
            self.num_inhabitant += n # a += n is equivalent to a = a + n
        else:
            raise Exception("The number of added inhabitants cannot be negative")

    def rmInhabitants(self, n):
        if n >= 0:        
            if n <= self.num_inhabitant:
                self.num_inhabitant -= n # a -= n is equivalent to a = a - n
            else:
                raise Exception("The number of removed inhabitants cannot be greater than the current number of inhabitants")
        else:
            raise Exception("The number of removed inhabitants cannot be negative")
        
    
if __name__ == "__main__":
    p1 = Point(0, 5)
    p2 = Point(-1, 9)
    print(p1)
    print(p2)
    print(Point.cartesianDistance(p1, p2))
    nantes = City(47, -2, "Nantes", 303382)
    print(nantes)
    nantes.addInhabitants(29035)
    print(nantes)