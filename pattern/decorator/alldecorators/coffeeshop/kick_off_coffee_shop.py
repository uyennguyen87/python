from pattern.decorator.alldecorators.coffeeshop.Chocolate import Chocolate
from pattern.decorator.alldecorators.coffeeshop.SteamedMilk import SteamedMilk
from pattern.decorator.alldecorators.coffeeshop.Espresso import Espresso
from pattern.decorator.alldecorators.coffeeshop.FoamedMilk import FoamedMilk
from pattern.decorator.alldecorators.coffeeshop.Mug import Mug
from pattern.decorator.alldecorators.coffeeshop.Whipped import Whipped

def make_menu():
    cappuccino = Espresso(FoamedMilk(Mug()))
    cafeMocha = Espresso(SteamedMilk(Chocolate(Whipped(Mug()))))
    menu = [cappuccino, cafeMocha]
    return menu

if __name__ == '__main__':
    menu = make_menu()
    for drink in menu:
        print drink.get_description(), ': $', drink.get_total_cost()