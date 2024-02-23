from plant import Plant
import random


class VenusFlytrap(Plant):

    def catch(self, energy_amount: int) -> int:
        random_int = random.randint(1, 4)
        if random_int in range(3):
            print("A successful catch!")
            self.energy += energy_amount
            return self.energy
        elif energy_amount < 0:
            print("Dangerous! Do not eat.")
            return self.energy
        else:
            print("Oh dear. Better luck next time.")
            return self.energy