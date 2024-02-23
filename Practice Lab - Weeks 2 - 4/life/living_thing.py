

class LivingThing:
    MAX_ENERGY = 100

    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def grow(self) -> int:
        """Increase age attribute by 1."""
        self.age += 1
        return self.age

    def reproduce(self) -> bool:
        """Assess current energy levels. Reproduce if over 20 and decrease energy, return true.
        Else, return false and print appropriate message."""
        if self.energy >= 20:
            can_produce = True
            self.energy -= 20
            print(f'{self.name} has reproduced, they have {self.energy} points left')
        else:
            can_produce = False
            print(f'{self.name} does not have enough points for this action')
        return can_produce