from update_order import UpdateOrder
from create_order import CreateOrder
from ship_order import ShipOrder
from no_command import NoCommand
import sys


def get_commands():
    commands= (CreateOrder,UpdateOrder,ShipOrder)
    return { cls.name:cls for cls in commands}
    
# used where no command are supplied
def print_usage(commands):
    print("Usage : python -m afterCommand CommandName [arguments]")
    print('COmmands :')
    for command in commands.values:
        print("{}".format(command.description))

def parse_command(commands,args):
    command = commands.setdefault(args[0],NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

# Find and exectue command
command = parse_command(commands,sys.argv[1:])
command.execute()