from abc import ABC
from project.food import Meat, Vegetable, Fruit, Seed
from project.animals.animal import Mammal


class Mouse(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_list = [Vegetable, Fruit]
        self.sound = "Squeak"
        self.weight_gain = 0.10

    def make_sound(self):
        return self.sound


class Dog(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_list = [Meat]
        self.sound = "Woof!"
        self.weight_gain = 0.40

    def make_sound(self):
        return self.sound


class Cat(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_list = [Vegetable, Meat]
        self.sound = "Meow"
        self.weight_gain = 0.30

    def make_sound(self):
        return self.sound


class Tiger(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_list = [Meat]
        self.sound = "ROAR!!!"
        self.weight_gain = 1

    def make_sound(self):
        return self.sound