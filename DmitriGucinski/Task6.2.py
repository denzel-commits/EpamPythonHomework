class HistoryDict:
    _dictionary = {}
    _history_keys = []
    def __init__(self, dictionary):
        self._dictionary = dictionary
    
    def set_value(self, key, value):
        self._dictionary[key] = value        
        self._history_keys.append(key)
        
        self._history_keys = self._history_keys[-10:]
            
        
    def get_history(self):
        return self._history_keys
        

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("fera", 44)
d.set_value("roba", 45)
d.set_value("zero", 46)
d.set_value("fora", 47)
d.set_value("laba", 48)
d.set_value("true", 49)
d.set_value("false", 50)
d.set_value("laky", 51)
d.set_value("olaf", 52)
d.set_value("buter", 53)
d.set_value("orbit", 54)
print(
    d.get_history()
)
