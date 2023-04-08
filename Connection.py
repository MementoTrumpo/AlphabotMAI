from enum import Enum, unique

@unique
class EConnectionState(Enum):
    DISCONNECTED = 1,
    CONNECTING = 2,
    CONNECTED = 3
    
    
class Connection():
    
    def __init__(self, connection : str):
        self.__connection
    
    
    
    

