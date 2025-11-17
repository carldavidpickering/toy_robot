''' Command object factory written for Toy Robot Simulator
Carl Pickering 16th November 2025'''

class CommandObjectFactory:
    '''This class contains the parser to convert command lines into objects and the 
    functions to process them.'''
    def __init__(self, command_list):
        self.command_list = command_list

    def command_parser(self, commandline):
        ''' Take in command line and return command object to process it. The
        command object doesn't know the status of the robot before parsing. 
        Processing is handled separately. This way if necessary commands could
        be queued up.
        If the command is not recognised or blank it is ignored.'''
        separated_command = commandline.split()
        if len(separated_command)==0:
            return None
        if len(separated_command)==1:
            args=""
        else:
            args = separated_command[1]

        #print("separated command=", separated_command)
        handler = self.command_list[separated_command[0]]
        #print(commandline)
        return handler(self,args)
