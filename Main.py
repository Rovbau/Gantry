from Stepper import *
from Parser import *

parser = Parser()
stepper_x = Stepper("Axis X", mm_per_step = 0.10, pin_dir = 35, pin_step = 37, actual=0)
stepper_y = Stepper("Axis Y", mm_per_step = 0.10, pin_dir = 31, pin_step = 33, actual = 0)

    
parser.command_from_file("commands.txt")
pprint.pp(parser.commands)

for code in parser.commands:
    if code["move_code"] == "X":
        stepper_x.goto_pos(int(code["value"]))
    elif code["move_code"] == "Y":
        stepper_y.goto_pos(int(code["value"]))
    elif code["move_code"] == "SLEEP":
        print("Sleep %s" % (int(code["value"])))
        sleep(int(code["value"]))
    elif code["move_code"] == "#":
        print("Info: %s" % code["value"])
print("Ende")
