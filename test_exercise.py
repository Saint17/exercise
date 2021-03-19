import pytest
from exercise import Car, Direction

def test_isMoving():
    test_car = Car()
    test_car.moveForward()
    assert test_car.isMoving()

def test_forward():
    test_car = Car()
    test_car.moveForward()
    assert test_car.direction == Direction.FORWARD

def test_backward():
    test_car = Car()
    test_car.moveBackward()
    assert test_car.direction == Direction.REVERSE

def test_stop():
    test_car = Car()
    test_car.moveBackward()
    test_car.stop()
    assert not test_car.isMoving()