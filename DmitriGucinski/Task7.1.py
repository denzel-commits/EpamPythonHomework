#context manager class-based
# better then just use try ... finally to close connection. close file before exception

class FileResource:
    
    def __init__(self, filename, mode = 'r'):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
       try: 
           self.handler = open(self.filename, self.mode)           
           return self.handler
       except OSError as err:
           print(f"File open error {err}")
           raise err   
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.handler.close()
        print(f"File is closed = {self.handler.closed}")
        print(f"Resource exits = {(exc_type, exc_value, exc_tb)}")
        return True # return True to suppress exception
        
        
with FileResource('hello.txt', 'r') as file:
    file.write('test row')
