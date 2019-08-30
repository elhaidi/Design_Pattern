from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand
class CreateOrder:
    name ='CreateOrder'
    description = 'Create an Order'

    def execute(self):
        print(" Executing creating the order")