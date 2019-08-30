
class CommandExecutor:
    
    def execute_command(self,*args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.upadate_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print('\n**********************')
            print('Command uncategorized')   
            print('**********************\n')
    def create_order(self):
        pass
    
    def upadate_quantity(self,val):
        print(val)
        old_val = 5
        print('DataBase updated')
        print('Logging updated quantity from {} to {}'.format(old_val,val))

    def ship_order(self):
        pass