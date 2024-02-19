import unittest
from human import Human
from planet import Planet


class TestPlanet(unittest.TestCase):
    def test_add_human(self):
        # Check for 0 population.
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # Check a single human can be added.
        human_joe = Human('Joe')
        self.assertEqual(earth.add(human_joe), True, "Method should return True.")

    def test_remove_human(self):
        # Check that humans can be removed.
        human_joe = Human('Joe')
        earth = Planet('Earth')
        earth.add(human_joe)
        self.assertEqual(earth.remove(human_joe), False, "Method should return False.")

    def test_has_human(self):
        # Check the planet does have a specified human.
        human_joe = Human('Joe')
        earth = Planet('Earth')
        earth.add(human_joe)
        self.assertEqual(earth.has(human_joe), True, "Method should return True.")

        # Check that the planet does not have a specified human.
        human_bill = Human('Bill')
        self.assertEqual(earth.has(human_bill), False, "Method should return False.")


if __name__ == '__main__':
    unittest.main()