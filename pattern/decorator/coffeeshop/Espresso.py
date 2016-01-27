from pattern.decorator.coffeeshop.Decorator import Decorator


class Espresso(Decorator):
    cost = 0.74

    def __init__(self, component):
        Decorator.__init__(self, component)

