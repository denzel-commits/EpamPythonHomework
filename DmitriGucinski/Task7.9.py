from collections.abc import Iterable

class EvenRange():    
    _index = 0 
    
    def __init__(self, start, end):
           
        self.start = start
        self.end = end                
           
        self.collection = self.init_collection()                                      
        self.even_collection = [e for e in self.collection if e%2 == 0] 
        
    def init_collection(self):

       if not isinstance(self.start, int):
           raise TypeError("NumberCollection supports only integer numbers!")
        
       if not isinstance(self.end, int):
           raise TypeError("NumberCollection supports only integer numbers!")            

       return self.fill_collection()
        
    def fill_collection(self):
                               
        tcollection = []      
        
        n = self.start
        
        while n <= self.end:
            tcollection.append(n)
            n += 1        
           
        return tcollection
        
    def __str__(self):
        return ' '.join(str(e) for e in self.even_collection)
        
    def __iter__(self):        
        self._index = 0
        return self
    
    def __next__(self):
        while self._index < len(self.collection):            
            if self.collection[self._index]%2 == 0:
                result = self.collection[self._index] 
                self._index += 1            
                return result                        
            self._index += 1    
        else:
            raise StopIteration("Out of numbers!")
        
a = EvenRange(7,11)        
print(a)
print(
next(a)
)
print(
next(a)
)
print(
next(a)
)
