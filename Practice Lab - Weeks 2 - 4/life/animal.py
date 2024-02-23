from living_thing import LivingThing


class Animal(LivingThing):
    def eat(self, amount: int) -> int:
        """Take an input energy consumption input, add it to current energy attribute. Return excess over max energy."""
        self.energy += amount
        excess = self.energy - LivingThing.MAX_ENERGY
        print(f'{self.name} has {excess} excess energy')
        return excess

    def move(self, distance: int) -> bool:
        """Take a distance input, and times it by energy cost. If total energy cost is less than current energy levels,
        perform a move action, decreasing energy, returning true. Else, return false and print appropriate message."""
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