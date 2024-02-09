import unittest
from human import Human


class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_prins = Human("Prins")
        self.assertEqual(human_prins.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_prins = Human("Prins", energy=90)
        self.assertEqual(human_prins.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat exactly what is required
        human_prins = Human("Prins", energy=80)
        self.assertEqual(human_prins.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_prins = Human("Prins", energy=70)
        self.assertEqual(human_prins.eat(20), -10, "Excess should be -10.")

    def test_grow(self) -> None:
        # Age increments appropriately
        human_prins = Human("Prins", age=25)
        self.assertEqual(human_prins.grow(), 26, "Age should increment by 1.")

    def test_reproduce(self) -> None:
        # human has enough energy and can reproduce.
        human_prins = Human("Prins", energy=40)
        self.assertEqual(human_prins.reproduce(), True, "Energy should decrease by 20.")

        # human does not have enough energy, they cannot reproduce.
        human_prins = Human("Prins", energy=15)
        self.assertEqual(human_prins.reproduce(), False, "Energy should decrease by 20.")

    def test_move(self) -> None:
        # human has enough energy and can move.
        human_prins = Human("Prins", energy=10)
        self.assertEqual(human_prins.move(1), True, "Energy should decrease by 20.")

        # human does not have enough energy, they cannot reproduce.
        human_prins = Human("Prins", energy=10)
        self.assertEqual(human_prins.move(2), False, "Energy should decrease by 20.")


if __name__ == '__main__':
    unittest.main()