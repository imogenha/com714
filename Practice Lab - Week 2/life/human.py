class Human:
    MAX_ENERGY = 100

    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old, and has {self.energy} energy'

    def grow(self) -> int:
        self.age += 1
        return self.age

    def eat(self, amount: int) -> int:
        self.energy += amount
        excess = self.energy - Human.MAX_ENERGY
        print(f'{self.name} has {excess} excess energy')
        return excess

    def reproduce(self) -> bool:
        if self.energy >= 20:
            can_produce = True
            self.energy -= 20
            print(f'{self.name} has reproduced, they have {self.energy} points left')
        else:
            can_produce = False
            print(f'{self.name} does not have enough points for this action')
        return can_produce

    def move(self, distance: int) -> bool:
        move_energy = 10
        total_energy = move_energy * distance
        if self.energy >= total_energy:
            self.energy -= total_energy
            can_move = True
            print(f'{self.name} has moved. They have {self.energy} energy points left')
        else:
            can_move = False
            print(f'{self.name} has no energy to move!')
        return can_move


h1 = Human("John", 28, 70)

