from collections.abc import Iterable

class MyNumberCollection():    
    _index = 0 
    
    def __init__(self, start, end=0, step=0):
           
        self.start = start
        self.end = end
        self.step = step                     
           
        self.collection = self.init_collection()                                      
        
    def init_collection(self):
        if isinstance(self.start, Iterable):
           return self.fill_collection_with_iterable()
        else:               
                    
           if not isinstance(self.start, int):
               raise TypeError("NumberCollection supports only integer numbers!")
            
           if not isinstance(self.end, int):
               raise TypeError("NumberCollection supports only integer numbers!")            
        
           if not isinstance(self.step, int):
               raise TypeError("NumberCollection supports only integer numbers!")
            
           return self.fill_collection()
        
    def fill_collection(self):
                               
        tcollection = []      
        for n in range(self.start, self.end+1, self.step):
            tcollection.append(n)
        
        if self.end not in tcollection:
            tcollection.append(self.end)  
            
        return tcollection
            
    def fill_collection_with_iterable(self):
        tcollection = []
        for n in self.start:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError("NumberCollection supports only numbers!")
            
            tcollection.append(n)
        
        return tcollection
                
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.collection):
            result = self.collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
            
    def __add__(self, other):
        return self.collection + other.collection        
    
    def __getitem__(self, index):
        return self.collection[index] ** 2           
    
    def __str__(self):
        return ''.join(map(str, self.collection)) # return ''.join(str(e) for e in self.collection)
        
    def append(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("'{}' - object is not a number!".format(value))
        
        return self.collection.append(value)
        
        

a = MyNumberCollection(4,310,2)
a.append(56)
a.append(56.12)

for elem in a:
    print(elem)        
        

