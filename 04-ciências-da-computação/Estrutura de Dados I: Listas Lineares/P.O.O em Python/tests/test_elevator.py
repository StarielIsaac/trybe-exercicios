from elevator_system.elevator import Elevator, ElevatorStatus
from elevator_system.motor import Motor, MotorSide
from unittest.mock import patch


def test_create_elevator():
    motor = Motor()
    elevator = Elevator(motor)
    assert elevator.current_floor == 0
    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.STOPPED


@patch("time.sleep", return_value=None)
def test_move_up(self):
    elevator = Elevator(Motor())
    destination_floor = 5
    elevator.move(destination_floor)

    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_UP
    assert elevator.current_floor == destination_floor
    assert elevator.motor.side == MotorSide.CLOCKWISE


@patch("time.sleep", return_value=None)
def test_move_going_down(self):
    # Triplice do Teste
    # Triple AAA
    # Cenário / Arrange
    elevator = Elevator(Motor())
    elevator.current_floor = 5

    # Ação / Act
    destination_floor = 1
    elevator.move(destination_floor)

    # Analise / Assertion
    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_DOWN
    assert elevator.current_floor == destination_floor
    assert elevator.motor.side == MotorSide.ANTICLOCKWISE


def test_move_same_floor():
    elevator = Elevator(Motor())
    elevator.current_floor = 5

    destination_floor = elevator.current_floor

    elevator.move(destination_floor)

    assert elevator.door_is_open is True
    assert elevator._status == ElevatorStatus.STOPPED
    assert elevator.current_floor == destination_floor
