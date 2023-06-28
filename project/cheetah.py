from project.animal import Animal


class Cheetah(Animal):
    PERSONAL_MONEY_TO_CARE = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.PERSONAL_MONEY_TO_CARE)
