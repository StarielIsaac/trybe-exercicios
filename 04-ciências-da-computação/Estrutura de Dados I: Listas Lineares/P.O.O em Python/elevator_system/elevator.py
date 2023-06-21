from enum import Enum

from elevator_system.motor import MotorSide
from elevator_system.motorized_equipment import MotorizedEquipment


class Elevator(MotorizedEquipment):
    def __init__(self, motor):
        super().__init__(motor)

        # self.motor = motor # Composição
        self.current_floor = 0
        self.door_is_open = False
        self._status = ElevatorStatus.STOPPED

    def move(self, destination_floor):
        if self.current_floor == destination_floor:
            self.door_is_open = True
            self._status = ElevatorStatus.STOPPED
            return

        self.door_is_open = False

        if destination_floor > self.current_floor:
            self.__up(destination_floor)
        else:
            self.__down(destination_floor)

    def __down(self, destination_floor):
        self._status = ElevatorStatus.GOING_DOWN
        time_to_work = abs(destination_floor - self.current_floor)
        self.backward(time_to_work)
        self.current_floor = destination_floor

    def __up(self, destination_floor):
        self._status = ElevatorStatus.GOING_UP
        time_to_work = abs(destination_floor - self.current_floor)
        self.forward(time_to_work)
        self.current_floor = destination_floor

    # Decorator Python
    @property
    def status(self):
        # if(Autenticado_como_pessoa_tecnica == True):
        return self._status

    @status.setter
    def status(self, new_status):
        # if(Autenticado_como_pessoa_tecnica == True):
        self._status = new_status


class ElevatorStatus(Enum):
    STOPPED = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOCKED = 3


# x = Elevator()
# print(x.get_status)
# x.set_status(ElevatorStatus.GOING_DOWN)

# print(x.status)
# x.status = ElevatorStatus.GOING_DOWN
