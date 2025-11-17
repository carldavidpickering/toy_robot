"""
command_line_interface

A basic command line interface to allow for user interaction.
"""
from sys import stdin, stdout, stderr
from toy_robot import Robot, CommandObjectFactory, RobotCommandMakers
from table import Table

class CommandLineInterface:
    """ Provides a command line interface."""
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
            if command_object is not None:
                command_object.execute(self.robot)
        except KeyError:
            self.error_file.write("ERROR: Command not recognised:"+command_line+"\n")
        except Exception as e:
            self.error_file.write("ERROR: Other error: "+str(e)+"\n")
        return True


if __name__=="__main__":
    cli = CommandLineInterface(stdin, stdout, stdout)
    while cli.process_command():
        print(">")
