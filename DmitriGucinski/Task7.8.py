
class MySquareIterator:
    i = 0
    
    def __init__(self, lst):
        self.lst = lst
        
    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i < len(self.lst):
            result = self.lst[self.i] ** 2
            self.i += 1
            return result
        else:
            raise StopIteration

lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
