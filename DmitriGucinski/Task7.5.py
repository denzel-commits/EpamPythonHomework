class CustomBaseException(BaseException):
    def __init__(self, message=""):
        if message:
            self.message = message
        else:    
            self.message = "Uknown error occured"

    def __str__(self):
        return "Exception: {}".format(self.message)
        
class NotEvenException(CustomBaseException):
    def __init__(self, message=""):
        if message:
            self.message = message
        else: 
            self.message = "Number provided is not even"
        
class LessThreeException(CustomBaseException):
    def __init__(self, message=""):
        if message:
            self.message = message
        else: 
            self.message = "Number provided is less than 3 but should be at least 3."


class EvenNumbers:
    def __init__(self, num):
        self.num = num
        
    def is_even(self):
        if self.num < 3:
            raise LessThreeException
            
        if self.num%2 != 0:
            raise NotEvenException
        
        return True    
            

try:
    num = 2
    check = EvenNumbers(num)
    if check.is_even():
        print("{} is even".format(num))
except LessThreeException as err:
    print("Error {}".format(err) )
except NotEvenException as err:                      
    print("Error {}".format(err) )
    
        
    
