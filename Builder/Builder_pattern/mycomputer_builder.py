from abs_builder import AbsBuilder

class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case= 'Coolemaster'

    def build_mainboard(self):
        self._computer.mainboard='MSI 970'
        self._computer.cpu='IntelCOre i7'
        self._computer.memory='Corsair 16 GB'

    def install_mainboard(self):
        pass
    
    def installl_hard_drive(self):
        self._computer.hard_drive='Seagate 2TB'
    
    def install_video_card(self):
        self._computer.video_card='Geforce GTX 1070'