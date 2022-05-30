from contextlib import contextmanager

@contextmanager
def resource_manager(filename, mode = "r"):
    try:   
        file = open(filename, mode)                    
        yield file
        file.close()           
    except OSError as err:
        print(f'Error occured {err}')            
        
with resource_manager('hello72.txt', 'r') as file:
    file.write('test row')
        
