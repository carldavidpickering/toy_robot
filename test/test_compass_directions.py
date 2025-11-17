import pytest
from compass_directions import CompassDirections

def test_compass_directions_constructor():
    pass
    d = CompassDirections("SOUTH")
    assert d == CompassDirections.SOUTH
    d = CompassDirections("NORTH")
    assert d == CompassDirections.NORTH
    d = CompassDirections("EAST")
    assert d == CompassDirections.EAST
    d = CompassDirections("WEST")
    assert d == CompassDirections.WEST
    with pytest.raises(ValueError):
        d = CompassDirections("UP")
    with pytest.raises(ValueError):
        d = CompassDirections("")

def test_compass_directions_assign():
    d = CompassDirections.NORTH
    assert d==CompassDirections("NORTH")
    d = CompassDirections.SOUTH
    assert d==CompassDirections("SOUTH")
    d = CompassDirections.EAST
    assert d==CompassDirections("EAST")
    d = CompassDirections.WEST
    assert d==CompassDirections("WEST")

def test_compass_directions_rotate_left():
    d = CompassDirections(CompassDirections.NORTH)
    assert d.whats_left()==CompassDirections.WEST
    d = CompassDirections.WEST
    assert d.whats_left()==CompassDirections.SOUTH
    d =CompassDirections.SOUTH
    assert d.whats_left()==CompassDirections.EAST
    d =CompassDirections.EAST
    assert d.whats_left()==CompassDirections.NORTH

def test_compass_directions_rotate_right():
    d = CompassDirections(CompassDirections.NORTH)
    assert d.whats_right()==CompassDirections.EAST
    d = CompassDirections.EAST
    assert d.whats_right()==CompassDirections.SOUTH
    d =CompassDirections.SOUTH
    assert d.whats_right()==CompassDirections.WEST
    d =CompassDirections.WEST
    assert d.whats_right()==CompassDirections.NORTH