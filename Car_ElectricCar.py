class Car:
    def __init__(self, brand, model, year, speed=0, fuel=0):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed
        self._fuel = fuel

    def get_brand(self):
        return self._brand
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year
    def get_speed(self):
        return self._speed
    def get_fuel(self):
        return self._fuel
    
    def set_speed(self, speed):
        self._speed = speed
    def set_fuel(self, fuel):
        self._fuel = fuel

    def accelerate(self, amount):
        if self._fuel > 0:
            self._speed += amount
            self._fuel -= amount * 0.1
            if self._fuel < 0:
                self._fuel = 0

    def brake(self, amount):
        self._speed = max(0, self._speed - amount)

    def get_info(self):
        return f"{self._brand} {self._model}, {self._year}, speed={self._speed}, fuel={self._fuel}"

    def refuel(self):
        self._fuel = 100


class ElectricCar(Car):
    def __init__(self, brand, model, year, speed=0, battery_level=100):
        super().__init__(brand, model, year, speed, fuel=0)
        self._battery_level = battery_level

    def accelerate(self, amount):
        if self._battery_level > 0:
            self._speed += amount
            self._battery_level -= amount * 0.2
            if self._battery_level < 0:
                self._battery_level = 0

    def charge(self):
        self._battery_level = 100

    def get_range(self):
        return self._battery_level * 2  # условный запас хода


    def __str__(self):
        return f"Car: {self._brand} {self._model}, speed={self._speed}"
    def __mul__(self, other):
        return self._speed * other
    def __sub__(self, other):
        return abs(self._speed - other._speed)
    def __le__(self, other):
        return self._year <= other._year



car1 = Car("Toyota", "Camry", 2020, fuel=50)
car2 = ElectricCar("Tesla", "Model 3", 2022)

car1.accelerate(20)
car2.accelerate(30)

print(car1.get_info())
print(car2.get_range())

print(str(car2))
print(car2 * 2)
print(car2 - car1)
