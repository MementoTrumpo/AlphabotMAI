from enum import Enum, unique

@unique
class EStateRobot(Enum):
    IDLE = 1,
    FORWARD = 2,
    ROTATE = 3