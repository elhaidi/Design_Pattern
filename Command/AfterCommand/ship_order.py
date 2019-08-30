from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand
class ShipOrder:
    name ='ShipOrder'
    description = 'Shiep ypur order'

    def execute(self):
        print('Exectuing the Shipping')