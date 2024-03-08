class ComplexNumbers:
    
    # a + i * b with i**2 == -1
    def __init__(self, a, b):
        self._a = a
        self._b = b
        
    def getA(self):
        return self._a
        
    def getB(self):
        return self._b
    
    def __add__(self, complex):
        return ComplexNumbers(self._a + complex.getA(), self._b + complex.getB())
