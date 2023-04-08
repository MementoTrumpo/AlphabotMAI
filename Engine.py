from EngineState import EngineState

class Engine():
    #Инициализация двигаеля
    def __init__(self, state: EngineState):
        self._state = state
        
    #Установка состояния двигателя
    def set_state(self, state : EngineState):
        self._state = state
      
    #Получение сотояния двигателя  
    def get_state(self):
        return self._state
    