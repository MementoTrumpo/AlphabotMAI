from StateRobot import EStateRobot

'''class Finite state machine'''
class System:
    
    '''Inicializing object Finite state machine'''
    def __init__(self, state : EStateRobot):
        self.__state = state;
        
    
    '''Getting the status value'''
    def get_state(self):
        return self.__state
    
    '''Setting the status value'''
    def set_state(self, state):
        self.__state = state

    
    # '''Updating the machine status'''
    # def update(self):
    #     if(self.__state != None):
    #         self.__state = self
    #     else:
    #         raise Exception()
    
    
            