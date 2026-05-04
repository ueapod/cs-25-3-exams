class Restaurant:
    def __init__(self, name, cuisine, rating, menu, tables):
        self._name = name
        self._cuisine = cuisine
        self._rating = rating
        self._menu = menu
        self._tables = tables

    def get_name(self):
        return self._name

    def get_rating(self):
        return self._rating

    def set_rating(self, r):
        self._rating = r

    def add_dish(self, dish):
        self._menu.append(dish)

    def remove_dish(self, dish):
        if dish in self._menu:
            self._menu.remove(dish)

    def get_average_price(self):
        if len(self._menu) == 0:
            return 0
        s = 0
        for i in self._menu:
            s += i[1]
        return s / len(self._menu)

    def reserve_table(self, count):
        if count <= self._tables:
            self._tables -= count
            return "ok"
        return "no"

    def make_order(self, i):
        if 0 <= i < len(self._menu):
            return "you ordered " + self._menu[i][0]
        return "error"

    def __str__(self):
        return f"Restaurant: {self._name} ({self._cuisine}, {self._rating})"

    def __gt__(self, other):
        return self._rating > other._rating

    def __getitem__(self, i):
        return self._menu[i]

    def __iter__(self):
        return iter(self._menu)

class FastFood(Restaurant):
    def __init__(self, name, cuisine, rating, menu, tables, delivery, time):
        super().__init__(name, cuisine, rating, menu, tables)
        self._delivery = delivery
        self._time = time

    def get_average_price(self):
        return super().get_average_price() * 0.7

    def order_for_delivery(self, i):
        if self._delivery and 0 <= i < len(self._menu):
            return f"delivery {self._menu[i][0]} in {self._time} min"
        return "no delivery"

    def reserve_table(self, count):
        return "no reserve"

    def make_order(self, i):
        if 0 <= i < len(self._menu):
            return "fastfood order " + self._menu[i][0]
        return "error"