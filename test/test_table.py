
import pytest
from table import Table

def test_table_valid_constructor():
    t = Table(6,5)
    assert t.get_x_max()==5
    assert t.get_y_max()==4

def test_table_negative_size():
    with pytest.raises(ValueError):
        t = Table(-1,3)
    with pytest.raises(ValueError):
        t = Table(2,-2)

def test_table_zero_size():
    with pytest.raises(ValueError):
        t = Table(0,3)
    with pytest.raises(ValueError):
        t = Table(2,0)

def test_table_bounds():
    t = Table(4,4)
    assert(True==t.is_valid_position(0,0))
    assert(True==t.is_valid_position(1,2))
    assert(True==t.is_valid_position(3,3))
    assert(False==t.is_valid_position(4,3)) 
    assert(False==t.is_valid_position(3,4)) 
    assert(False==t.is_valid_position(-1,3)) 