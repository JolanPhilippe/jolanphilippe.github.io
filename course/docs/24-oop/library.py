class Library:
    
    def __init__(self, name, address, size, rank):
        self.__name = name
        self.address = address
        self.size = size
        self.rank = rank
        self.shelves = []
        
    def get_name(self):
        return self.__name
        
    def set_name(self, new_name):
        if new_name != "":
            raise Exception("Empty names are not allowed")
        self.__name = new_name
    
    def __str__(self):
        result = f"{self.name} ({self.address})"
        for shelf in self.shelves:
            result += f"\n- Shelf number {shelf.number}:"
            for book in shelf.books:
                result += f"\n\t- {book.title}"
        return result
    
    
    def addShelf(self, shelf):
        self.shelves.append(shelf)
        
    def addShelfByNumber(self, number):
        empty_shelf = Shelf(number, 10)
        self.shelves.append(empty_shelf)
        return empty_shelf
    
    def _addBook(self, book, shelf_number):
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.addBook(book)
                return
        shelf = self.addShelfByNumber(shelf_number)
        shelf.addBook(book)
        
    
class Shelf:
    
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.books = []

    def __str__(self):
        return f"{self.number}"
    
    def addBook(self, book):
        if len(self.books) == self.size:
            raise Exception("Shelf is already full")
        else:
            self.books.append(book)
    
    
class Book:
    
    def __init__(self, title, author, release):
        self.title = title
        self.author = author
        self.releaseDate = release
    
    def __str__(self):
        pass
    

if __name__ == "__main__":
    library = Library("CARAE", "rue Alfred Kastler", 10, 10.0)
    book = Book("I Love Python", "Author", "04/03/2024")
    library.addBook(book, 10)
    print(library)
    library.set_name("New name")
    library.addBook()