from toy_robot import Robot, CommandObjectFactory, RobotCommandMakers
from table import Table
from sys import stdin, stdout, stderr

class CommandLineInterface:
    def __init__(self, input_file=stdin, output_file=stdout, error_file=stderr):
        self.input_file = input_file
        self.output_file = output_file
        self.error_file = error_file
        
        self.table = Table(5,5)
        self.robot = Robot(self.table)
        self.command_factory = CommandObjectFactory(RobotCommandMakers().command_list)

    def process_command(self):
        command_line = self.input_file.readline()
        command_line = command_line.rstrip()
        if command_line == "EXIT":
            return False
        try:
           command_object = self.command_factory.command_parser(command_line)
           if command_object!=None:
               command_object.execute(self.robot)
        except KeyError as e:
            self.error_file.write("ERROR: Command not recognised:"+command_line+"\n")
        except Exception as e:
            self.error_file.write("ERROR: Other error: "+e.__str__()+"\n")
        return True


if __name__=="__main__":
    processing_commands = True
    cli = CommandLineInterface(stdin, stdout, stdout) 
    while cli.process_command():
        print(">")
