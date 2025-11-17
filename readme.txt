Toy Robot Simulator
===================

Carl Pickering 17th November 2025
cdpickering@gmail.com
07773 325770

This is a toy robot simulator. To start it run:

python3 src/toy_robot_simulator.py

commands
========
The commands are:

PLACE X,Y,F
Where F=<NORTH,SOUTH,EAST,WEST>
x and y range from 0..4
Until PLACE is used none of the other commands have any effect.

MOVE
Moves one position forward

LEFT
Turns LEFT

RIGHT
Turns RIGHT

REPORT
Reports the current position and direction.


Issues
======
The toy_robot module is too complicated. The design splitting parsing from 
command execution is maybe taking it too far for the scope of this activity.

With more time this would be combined removing the RobotCommand classes would
go and call directly onto the methods in Robot from the handlers.

Notes
=====
trace.txt is a trace of moving around the table and not falling off the edges.