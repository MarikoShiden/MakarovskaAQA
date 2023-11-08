from abc import ABC, abstractmethod


class Dish(ABC):
    @abstractmethod
    def dish_name(self):
        pass

    @abstractmethod
    def dish_price(self):
        pass


class Pizza(Dish):
    def dish_name(self):
        return "Pizza"

    def dish_price(self):
        return 25


class Pasta(Dish):
    def dish_name(self):
        return "Pasta"

    def dish_price(self):
        return 18.5


class Risotto(Dish):
    def dish_name(self):
        return "Risotto"

    def dish_price(self):
        return 21


class Borsch(Dish):
    def dish_name(self):
        return "Borsch"

    def dish_price(self):
        return 50


class OrderPart:
    def __init__(self):
        self.items = []

    def add_item(self, dish):
        self.items.append(dish)

    def remove_item(self, dish):
        self.items.remove(dish)

    def calculate_total_price(self):
        total_price = sum(item.dish_price() for item in self.items)
        return total_price


order = OrderPart()
borsch = Borsch()
risotto = Risotto()
pizza = Pizza()

order.add_item(borsch)
order.add_item(pizza)
order.add_item(risotto)

price = order.calculate_total_price()
print(price)

order.remove_item(risotto)

price = order.calculate_total_price()
print(price)
