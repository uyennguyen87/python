from pattern.decorator.coffeeshop.Decorator import Decorator


class SteamedMilk(Decorator):
    cost = 0.25

    def __init__(self, component):
        Decorator.__init__(self, component)