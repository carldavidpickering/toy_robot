import pytest
from compass_directions import CompassDirections


def test_compass_directions_constructor():
    pass
    d = CompassDirections("SOUTH")
    assert d == CompassDirections.SOUTH

def test_compass_directions_rotate_left():
    d = CompassDirections(CompassDirections.NORTH)
    assert d.whats_left()==CompassDirections.WEST
    d = CompassDirections(CompassDirections.WEST)
    assert d.whats_left()==CompassDirections.SOUTH

