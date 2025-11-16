from enum import StrEnum

class Rotation(StrEnum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class Directions(StrEnum):
    # defined in an order such that right is clockwise and left anticlockwise
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

    directon = NORTH

    def __init(self):
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

    def turn_left(self):
        wegotit = self.whats_left()
        print("wegotit=", wegotit)
        self = wegotit
        print("Self direction = ", self)


class Table:
    x = 0
    y = 0

    def __init__(self, eastwest, northsouth):
        self.eastwest = eastwest
        self.northsouth = northsouth

class Robot:
    #direction = Directions()
    def __init__(self):
        pass
        self.direction = Directions(Directions.NORTH)

    def set_direction(self, direction):
        self.direction = direction

    def turn_left(self):
        newdirection = self.direction.whats_left()
        self.direction = newdirection
        print("New direction = ", self.direction.whats_left())
        
class RobotCommand:
    def __init__(self, args):
        self.args = args

    def Execute(self, robot):
        pass
    
class RobotPlaceCommand:
    def __init__(self, args):
       self.arg = args.split(",")
       print("args=", args)
       self.direction = Directions(args[2])

    def execute(self,robot):

        pass

class CommandObjectFactory:
    def handle_place(self, args):
        print("handle_place" , args)
        return RobotPlaceCommand(args)

    def handle_move(self, args):
        print("handle move")
        return RobotCommand(args)

    def handle_left(self, args):
        print("handle left")
        return RobotCommand(args)

    def handle_right(self, args):
        print("handle right")
        return RobotCommand(args)

    def handle_right(args):
        print("handle report")
        return RobotCommand(args)

    def handle_report(self, args):
        print("handle report")
        return RobotCommand(args)

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
           
       print("separated command=", separated_command)
       handler = self.command_list[separated_command[0]]
       print(commandline)
       return handler(self,args)
       

if __name__=='__main__':
        d = Directions("EAST")
        #d = Directions()
        d.turn_left()
        print("d=", d)
        r = Robot()
        print("robot currently", r.direction)
        r.turn_left()
        print("turned to", r.direction)
        a = CommandObjectFactory()
        c= a.command_handler("PLACE 2,3,W")
        c.execute(r)