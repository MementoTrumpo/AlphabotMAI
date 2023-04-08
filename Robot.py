from Detector import Detector
from StateRobot import EStateRobot
from EngineState import EngineState
from SimpleFSM import System

'''A class that implements the behavior of the robot'''
class Robot(System):
    
    def __init__(self, xCoord : float, yCoord : float, angle : float, state : EStateRobot):
        self.__xCoord = xCoord
        self.__yCoord = yCoord
        self.__angle = angle
        self.state = state
        self._engine_state =  EngineState.STOP
    
    @property
    def xCoord(self):
        return self.__xCoord
    
    @xCoord.setter
    def xCoord(self, xCoord):
        if(xCoord == None):
            raise ValueError("You cannot assign an empty property to an object")
        else:
            self.__xCoord = xCoord
    
    @property
    def yCoord(self):
        return self.__yCoord
    
    @yCoord.setter
    def yCoord(self, yCoord):
        if(yCoord == None):
            raise ValueError("You cannot assign an empty property to an object")
        else:
            self.__yCoord = yCoord
      
    @property
    def angle(self):
            return self.__angle
    
    @angle.setter
    def angele(self, angle):
        if(angle == None):
            raise ValueError("You cannot assign an empty property to an object")
        else:
            self.__angle = angle
    
    #Запуск двигателя после команды движения вперед
    def move_forward(self):
        self._engine_state = EngineState.START
        print('Engine state is: {0}'.format(self._engine_state))
    
    #Остановка двигателя после команды остановки двигателя
    def stop(self):
        self._engine_state = EngineState.STOP
        print('Engine state is: {0}'.format(self._engine_state))
    
    def rotate_by_given_angle(self, delta_angle : float):
        if(delta_angle == 0):
            print('Angle wasn''t be a zero!')
            
        elif(delta_angle < 0):
            self._engine_state = EngineState.ROTATE_LEFT
        
        else:
            self._engine_state = EngineState.ROTATE_RIGHT
        
    
    
    
      
    
    

    

      