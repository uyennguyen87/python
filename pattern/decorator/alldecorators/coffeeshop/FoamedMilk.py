from pattern.decorator.alldecorators.coffeeshop.Decorator import Decorator


class FoamedMilk(Decorator):
    cost = 0.25

    def __init__(self, component):
        Decorator.__init__(self, component)