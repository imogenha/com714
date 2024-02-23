from living_thing import LivingThing


class Plant(LivingThing):

    def __repr__(self) -> str:
        return f'plant(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def absorb(self, amount):
        self.energy += amount
        return self.energy
