''' Table for Toy Robot Simulator
Carl Pickering 16th November 2025'''
from enum import StrEnum
from abc import ABC, abstractmethod

class Rotation(StrEnum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

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
        #print(direction in Directions)
        #self.value = direction
        #self.name = direction
        #if direction.value for member in Directions:
        #    self.direction = direction

    def whats_left(self):
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
        match self.value:
            case Directions.NORTH:
                return Directions.WEST
            case Directions.WEST:
                return Directions.SOUTH
            case Directions.SOUTH:
                return Directions.EAST
            case Directions.EAST:
                return Directions.NORTH


class Table:
    def __init__(self, eastwest, northsouth):
        self.x_max = eastwest-1
        self.y_max = northsouth-1

    def get_x_max(self):
        return self.x_max

    def get_y_max(self):
        return self.y_max

class Robot:
    #direction = Directions()
    def __init__(self, table):
        self.table = table
        self.placed = False
        self.x = 0
        self.y = 0
        self.direction = Directions(Directions.NORTH)

    def set_direction(self, direction):
        self.direction = direction

    def turn_left(self):
        self.direction = self.direction.whats_left()

    def turn_right(self):
        self.direction = self.direction.whats_right()

    def move(self):
        if self.placed:
            match self.direction:
                case Directions.NORTH:
                    if self.y<self.table.get_y_max():
                        self.y = self.y + 1

                case Directions.SOUTH:
                    if self.y>0:
                        self.y = self.y - 1

                case Directions.EAST:
                    if self.x<self.table.get_x_max():
                        self.x = self.x + 1

                case Directions.WEST:
                    if self.x>0:
                        self.x = self.x - 1


    def place(self, x, y, f):
        if (x>self.table.get_x_max() or x<0):
            raise ValueError
        if (y>self.table.get_y_max() or y<0):
            raise ValueError
        self.direction=Directions(f)
        self.x = x
        self.y = y
        self.placed = True


class RobotCommand(ABC):
    def __init__(self, args=""):
        self.args = args

    @abstractmethod
    def execute(self, robot):
        pass

class RobotPlaceCommand(RobotCommand):
    ''' This class processes the PLACE command. We don't yet know the size of the table so 
        can't check that but will throw exceptions on wrong types x, y or f (facing)'''
    def __init__(self, args):
        parameters = args.split(",")
        print("parameters=", parameters)
        self.x = int(parameters[0])
        self.y = int(parameters[1])
        self.f = Directions(parameters[2])

    def execute(self,robot):
        robot.place(self.x, self.y, self.f)
        print("Robot placed")


class RobotReportCommand(RobotCommand):
    def execute(self, robot):
        print("REPORT ", robot.x, robot.y, robot.direction)


class RobotMoveCommand(RobotCommand):
    def execute(self, robot):
        robot.move()

class RobotRotateLeftCommand(RobotCommand):
    def execute(self, robot):
        robot.turn_right()

class RobotRotateRightCommand(RobotCommand):
    def execute(self, robot):
        robot.turn_right()

class CommandObjectFactory:
    def handle_place(self, args):
        print("handle_place" , args)
        return RobotPlaceCommand(args)

    def handle_move(self, args):
        print("handle move")
        return RobotMoveCommand(args)

    def handle_left(self, args):
        print("handle left")
        return RobotRotateLeftCommand(args)

    def handle_right(self, args):
        print("handle right")
        return RobotRotateRightCommand(args)

    def handle_report(self, args):
        print("handle report")
        return RobotReportCommand(args)

    command_list =  {
        "PLACE" : handle_place,
        "MOVE"  : handle_move,
        "LEFT"  : handle_left,
        "RIGHT" : handle_right,
        "REPORT" : handle_report
    }

    def command_handler(self, commandline):
        separated_command = commandline.split()
        if len(separated_command)==0:
            return
        if len(separated_command)==1:
            args=""
        else:
            args = separated_command[1]

        #print("separated command=", separated_command)
        handler = self.command_list[separated_command[0]]
        #print(commandline)
        return handler(self,args)


if __name__=='__main__':
    d = Directions("EAST")
    #d = Directions()
    #d.turn_left()
    d = d.whats_left()
    print("d=", d)
    t = Table(5,4)
    r = Robot(t)
    print("robot currently", r.direction)
    r.turn_left()
    print("turned to", r.direction)
    a = CommandObjectFactory()
    c= a.command_handler("PLACE 2,3,WEST")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("RIGHT")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)
    c = a.command_handler("MOVE")
    c.execute(r)
    c= a.command_handler("REPORT")
    c.execute(r)


    print(r)
