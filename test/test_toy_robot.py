
from sys import stdout, stdin, stderr
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

def test_move_when_not_placed():
    t = Table(5,4)
    r = Robot(t)
    assert 0 == r.x
    assert 0 == r.y
    r.move()
    assert 0 == r.x
    assert 0 == r.y

def test_move_north():
    t = Table(4,4)
    r = Robot(t)
    r.place(1,1,CompassDirections.NORTH)
    assert 1 == r.x
    assert 1 == r.y
    r.move()
    assert 1 == r.x
    assert 2 == r.y
    r.move()
    assert 1 == r.x
    assert 3 == r.y
    r.move()
    assert 1 == r.x
    assert 3 == r.y

def test_move_south():
    t = Table(4,4)
    r = Robot(t)
    r.place(1,2,CompassDirections.SOUTH)
    assert 1 == r.x
    assert 2 == r.y
    r.move()
    assert 1 == r.x
    assert 1 == r.y
    r.move()
    assert 1 == r.x
    assert 0 == r.y
    r.move()
    assert 1 == r.x
    assert 0 == r.y

def test_move_east():
    t = Table(4,4)
    r = Robot(t)
    r.place(1,2,CompassDirections.EAST)
    assert 1 == r.x
    assert 2 == r.y
    r.move()
    assert 2 == r.x
    assert 2 == r.y
    r.move()
    assert 3 == r.x
    assert 2 == r.y
    r.move()
    assert 3 == r.x
    assert 2 == r.y

def test_move_west():
    t = Table(4,4)
    r = Robot(t)
    r.place(2,2,CompassDirections.WEST)
    assert 2 == r.x
    assert 2 == r.y
    r.move()
    assert 1 == r.x
    assert 2 == r.y
    r.move()
    assert 0 == r.x
    assert 2 == r.y
    r.move()
    assert 0 == r.x
    assert 2 == r.y

def test_out_of_bounds_place_xy_dir():
    t = Table(4,4)
    r = Robot(t)
    with pytest.raises(ValueError):
        r.place(8,2,CompassDirections.WEST)
    assert 0 == r.x
    assert 0 == r.y
    assert CompassDirections.NORTH == r.direction

    with pytest.raises(ValueError):
        r.place(2,99,CompassDirections.WEST)
    assert 0 == r.x
    assert 0 == r.y
    assert CompassDirections.NORTH == r.direction

    with pytest.raises(ValueError):
        r.place(2,2,"UP")
    assert 0 == r.x
    assert 0 == r.y
    assert CompassDirections.NORTH == r.direction

def test_report_before_place(capsys):
    t = Table(4,4)
    r = Robot(t)
    r.report()
    captured = capsys.readouterr()
    assert captured.out==""

def test_report_after_place(capsys):
    t = Table(4,4)
    r = Robot(t)
    r.place(1,1,CompassDirections.EAST)
    assert 1==r.x
    assert True == r.placed

    r.report()
    captured = capsys.readouterr()
    assert captured.out=="REPORT 1,1,EAST\n"
    r.move()
    r.report()
    captured = capsys.readouterr()
    assert captured.out=="REPORT 2,1,EAST\n"
    r.turn_left()
    r.report()
    captured = capsys.readouterr()
    assert captured.out=="REPORT 2,1,NORTH\n"

