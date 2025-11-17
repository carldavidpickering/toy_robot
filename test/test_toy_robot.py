import pytest
from table import Table
from toy_robot import Robot
from compass_directions import CompassDirections

def test_constructor():
    t = Table(5,4)
    r = Robot(t)
    assert t == r.table
    assert False == r.placed
    assert CompassDirections.NORTH == r.direction
    assert 0 == r.x
    assert 0 == r.y
    print("robot currently", r.direction)
    r.turn_left()

def test_turn_left_when_not_placed():
    t = Table(5,4)
    r = Robot(t)
    assert CompassDirections.NORTH == r.direction
    r.turn_left()
    assert CompassDirections.NORTH == r.direction

def test_turn_left_when_placed():
    t = Table(5,4)
    r = Robot(t)
    assert CompassDirections.NORTH == r.direction
    r.place(1,1,CompassDirections.EAST)
    assert CompassDirections.EAST == r.direction
    r.turn_left()
    assert CompassDirections.NORTH == r.direction


def test_turn_right_when_not_placed():
    t = Table(5,4)
    r = Robot(t)
    assert CompassDirections.NORTH == r.direction
    r.turn_right()
    assert CompassDirections.NORTH == r.direction

def test_turn_right_when_placed():
    t = Table(5,4)
    r = Robot(t)
    assert CompassDirections.NORTH == r.direction
    r.place(1,1,CompassDirections.EAST)
    assert CompassDirections.EAST == r.direction
    r.turn_right()
    assert CompassDirections.SOUTH == r.direction
