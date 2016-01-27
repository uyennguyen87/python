from pattern.decorator.coffeeshop.DrinkComponent import DrinkComponent


class Decorator(DrinkComponent):
    def __init__(self, drink_component):
       self.component = drink_component

    def get_total_cost(self):
        base_cost = DrinkComponent.get_total_cost(self)
        extra_cost = self.component.get_total_cost()
        total_cost = base_cost + extra_cost
        return total_cost

    def get_description(self):
        return self.component.get_description() + \
            ' ' + DrinkComponent.get_description(self)
