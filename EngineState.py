from enum import Enum, unique

@unique
class EngineState(Enum):
    START = 1,
    STOP = 2
    ROTATE_LEFT = 3,
    ROTATE_RIGHT = 4