from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand,AbsOrderCommand):

    name = "UpdateQuantity"
    description = "UpdateQuantity number"

    def __init__(self,args):
        self.newqty= args[1]
    
    def execute(self):
        odlqty=5

        #Simulate database
        print('Updated database')

        # Simulate logging the  update
        print("Logggin updated quantity from {} to {}".format(odlqty,self.newqty))