import sys
from command_executor import CommandExecutor

if len(sys.argv) < 2:
    print('***********************\n')
    print("Usage python -m BeforeCOmmand <command>")
    print("Commands are :\n")
    print("\t CreateORder") 
    print("\t UpdateQuanttity number") 
    print("\t ShipOrder") 

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])