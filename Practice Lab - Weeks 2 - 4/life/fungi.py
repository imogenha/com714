from living_thing import LivingThing


class Fungi(LivingThing):

    def __init__(self, name: str, age: int = 0, energy: int = LivingThing.MAX_ENERGY, amount: int = 1) -> None:
        super(Fungi, self).__init__(name, age, energy)
        self.amount = amount

    def __repr__(self) -> str:
        return f'fungi(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def spread(self, increment: int) -> int:
        if increment < 0:
            print("Dangerous! Cannot implement.")
            return self.amount

        else:
            self.amount += increment
            return self.amount
