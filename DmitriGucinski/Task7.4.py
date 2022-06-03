from contextlib import suppress

def suppress_os(func):
    def wrapper(*args, **kwargs):
        with suppress(OSError):
            return func(*args, **kwargs)
    return wrapper  
    
def suppress_try(func):
    def wrapper(*args, **kwargs):       
        try:
            result = func(*args, **kwargs) 
            print('No exceptions')             
            return result
        except OSError as error:
            print("Suppressed error {error}")
            
    return wrapper       
    
@suppress_try   
def workload():
    with open("hello74.txt", 'r') as file:
        file.write('no errors')


workload()
