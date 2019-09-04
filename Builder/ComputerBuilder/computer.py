class Computer:

    def __init__(self,case,mainboard,cpu,memory,hard_drive,video_card):
        self.case=case
        self.mainboard= mainboard
        self.cpu=cpu
        self.memory=memory
        self.hard_drive=hard_drive
        self.video_card=video_card
    
    def display(self):
        print("\t {:>10} : {}".format('Case',self.case))
        print("\t {:>10} : {}".format('mainboard',self.mainboard))
        print("\t {:>10} : {}".format('CPU',self.cpu))
        print("\t {:>10} : {}".format('memory',self.memory))
        print("\t {:>10} : {}".format('hard_drive',self.hard_drive))
        print("\t {:>10} : {}".format('video_card',self.video_card))