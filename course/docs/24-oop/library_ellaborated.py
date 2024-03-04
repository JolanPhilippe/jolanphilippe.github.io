class Library:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.shelves = {}
        
    def __str__(self):
        return f"{self.name} ({self.address})"
    
    def __eq__(self, object):
        pass
    
    def addBook(self, book, shelf):
        if shelf not in self.shelves.keys():
            self.shelves[shelf] = set()    
        self.shelves[shelf].add(book)
            

class Shelf:
    
    def __init__(self, number):
        self.number = number
        
    def __str__(self):
        return f"Shelf n*{self.number}"    

 
class Book:
    
    def __init__(self, name, author, release):
        self.name = name
        self.author = author
        self.release = release
        
    def __str__(self):
        return f"{self.name}"
    
    def __eq__(self, object):
        if isinstance(object, Book):
            return self.name == object.name and self.author == object.author and self.release == object.release
        else:
            return False
    
