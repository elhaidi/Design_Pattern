from . import PROVIDER
from facade_factory import FacadeFactory

def main():
    facade = FacadeFactory.create_facade(PROVIDER)
    facade.get_employees()

    if __name__=__main__:
        main()