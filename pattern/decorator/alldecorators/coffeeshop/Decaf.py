from pattern.decorator.alldecorators.coffeeshop.Decorator import Decorator


class Decaf(Decorator):
    cost = 0.04

    def __init__(self, component):
        Decorator.__init__(self, component)