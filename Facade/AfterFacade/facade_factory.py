class FacadeFactory():
    @staticmethod
    def create_facade(module_name):
        module = import_module('.'+ module_name,__package__)
        classes = getmembers(module,
                             lambada m:(
                                 isclass(m)
                                 and not isabstract(m)
                                 andisublacc(m,AbsFacade)
                             )   
                                )
        return classes[0][1]()