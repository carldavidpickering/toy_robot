"""
toy_robot.py

Toy Robot Simulator for Cellular Origins
Carl Pickering 17th November 2025"""

from abc import ABC, abstractmethod
from command_factory import CommandObjectFactory
from compass_directions import CompassDirections
from table import Table
from sys import stdout, stdin, stderr

class Robot:
    '''This stores and operates on all the details of the robot position and status'''
    def __init__(self, table):
        self.table = table
        self.placed = False
        self.x = 0
        self.y = 0
        self.direction = CompassDirections(CompassDirections.NORTH)

    def set_direction(self, direction):
        self.direction = direction

    def turn_left(self):
        if self.placed:
            self.direction = self.direction.whats_left()

    def turn_right(self):
        if self.placed:
            self.direction = self.direction.whats_right()

    def move(self):
        if self.placed:
            match self.direction:
                case CompassDirections.NORTH:
                    if self.y<self.table.get_y_max():
                        self.y = self.y + 1

                case CompassDirections.SOUTH:
                    if self.y>0:
                        self.y = self.y - 1

                case CompassDirections.EAST:
                    if self.x<self.table.get_x_max():
                        self.x = self.x + 1

                case CompassDirections.WEST:
                    if self.x>0:
                        self.x = self.x - 1

    def place(self, x, y, f):
        if self.table.is_valid_position(x,y):
            self.direction=CompassDirections(f)
            self.x = x
            self.y = y
            self.placed = True
        else:
            raise ValueError("Initial position "+str(x)+","+str(y)+" Out of range.")

    def report(self):
        if self.placed:
            print("REPORT "+str(self.x)+","+str(self.y)+","+ str(self.direction))


class RobotCommand(ABC):
    '''The interface class from which we derive all our commands, this must not be instantiated.'''
    def __init__(self, args=""):
        self.args = args

    @abstractmethod
    def execute(self, robot):
        '''This each execute goes in here.'''

class RobotPlaceCommand(RobotCommand):
    ''' This class processes the PLACE command. We don't yet know the size of the table so 
        can't check that but will throw exceptions on wrong types x, y or f (facing)'''
    def __init__(self, args):
        parameters = args.split(",")
        self.x = int(parameters[0])
        self.y = int(parameters[1])
        self.f = CompassDirections(parameters[2])

    def execute(self,robot):
        robot.place(self.x, self.y, self.f)

class RobotReportCommand(RobotCommand):
    def execute(self, robot):
        robot.report()

class RobotMoveCommand(RobotCommand):
    def execute(self, robot):
        robot.move()

class RobotRotateLeftCommand(RobotCommand):
    def execute(self, robot):
        robot.turn_right()

class RobotRotateRightCommand(RobotCommand):
    def execute(self, robot):
        robot.turn_right()

class RobotCommandMakers:
    def handle_place(self, args):
        return RobotPlaceCommand(args)

    def handle_move(self, args):
        return RobotMoveCommand(args)

    def handle_left(self, args):
        return RobotRotateLeftCommand(args)

    def handle_right(self, args):
        return RobotRotateRightCommand(args)

    def handle_report(self, args):
        return RobotReportCommand(args)

    command_list =  {
        "PLACE" : handle_place,
        "MOVE"  : handle_move,
        "LEFT"  : handle_left,
        "RIGHT" : handle_right,
        "REPORT" : handle_report
    }




if __name__=='__main__':
    d = CompassDirections("EAST")
    #d = Directions()
    #d.turn_left()
    d = d.whats_left()
    print("d=", d)
    t = Table(5,4)
    r = Robot(t)
    print("robot currently", r.direction)
    r.turn_left()
    print("turned to", r.direction)
    a = CommandObjectFactory(RobotCommandMakers().command_list)
    c= a.command_parser("PLACE 2,3,WEST")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("RIGHT")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)
    c = a.command_parser("MOVE")
    c.execute(r)
    c= a.command_parser("REPORT")
    c.execute(r)


    print(r)
