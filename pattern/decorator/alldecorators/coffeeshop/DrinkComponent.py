class DrinkComponent:
    def get_description(self):
        return self.__class__.__name__
    def get_total_cost(self):
        return self.__class__.cost