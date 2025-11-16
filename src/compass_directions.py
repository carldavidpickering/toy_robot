'''Directions - A class to handle compass directions'''
from enum import StrEnum

class CompassDirections(StrEnum):
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
            case CompassDirections.NORTH:
                return CompassDirections.EAST
            case CompassDirections.EAST:
                return CompassDirections.SOUTH
            case CompassDirections.SOUTH:
                return CompassDirections.WEST
            case CompassDirections.WEST:
                return CompassDirections.NORTH

    def whats_right(self):
        '''Uses current direction to indicate where we would point if we
           turned right (clockwise).'''
        match self.value:
            case CompassDirections.NORTH:
                return CompassDirections.WEST
            case CompassDirections.WEST:
                return CompassDirections.SOUTH
            case CompassDirections.SOUTH:
                return CompassDirections.EAST
            case CompassDirections.EAST:
                return CompassDirections.NORTH
