from animal import Animal
from clothing import Clothing


class Human(Animal):

    def __init__(self, name: str, age: int = 0, energy: int = Animal.MAX_ENERGY) -> None:
        super(Human, self).__init__(name, age, energy)
        self.clothing = []

    def __repr__(self) -> str:
        return f'animal(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def dress(self, clothing: Clothing) -> bool:
        self.clothing.append(clothing)
        return clothing in self.clothing

    def undress(self, clothing: Clothing) -> bool:
        self.clothing.remove(clothing)
        return clothing in self.clothing