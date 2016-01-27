from pattern.decorator.coffeeshop.Chocolate import Chocolate
from pattern.decorator.coffeeshop.FoamedMilk import FoamedMilk
from pattern.decorator.coffeeshop.Mug import Mug
from pattern.decorator.coffeeshop.SteamedMilk import SteamedMilk
from pattern.decorator.coffeeshop.Whipped import Whipped

from pattern.decorator.coffeeshop.Espresso import Espresso


def make_menu():
    cappuccino = Espresso(FoamedMilk(Mug()))
    cafeMocha = Espresso(SteamedMilk(Chocolate(Whipped(Mug()))))
    menu = [cappuccino, cafeMocha]
    return menu

if __name__ == '__main__':
    menu = make_menu()
    for drink in menu:
        print drink.get_description(), ': $', drink.get_total_cost()