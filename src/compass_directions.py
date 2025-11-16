'''Directions - A class to handle compass directions'''
from enum import StrEnum

class Directions(StrEnum):
    '''Directions
    An enumerated type that provides compass directions with left and right rotations.
    '''
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

    def __init__(self, newdir=NORTH):
        pass

    def whats_left(self):
        '''Uses current direction to indicate where we would point if we
           turned left (anticlockwise).'''
        match self.value:
            case Directions.NORTH:
                return Directions.EAST
            case Directions.EAST:
                return Directions.SOUTH
            case Directions.SOUTH:
                return Directions.WEST
            case Directions.WEST:
                return Directions.NORTH

    def whats_right(self):
        '''Uses current direction to indicate where we would point if we
           turned right (clockwise).'''
        match self.value:
            case Directions.NORTH:
                return Directions.WEST
            case Directions.WEST:
                return Directions.SOUTH
            case Directions.SOUTH:
                return Directions.EAST
            case Directions.EAST:
                return Directions.NORTH
