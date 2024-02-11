from planet import Planet
from planet import NonPlanet
import random


class Universe:

    def __init__(self):
        self.__planets = []
        self.__nonplanets = []

    def generate(self) -> bool:
        items = [Planet, NonPlanet]
        selected_item = random.choice(items)
        if selected_item == Planet:
            planet = Planet()
            self.__planets.append(planet)
            return planet in self.__planets

        else:
            non_planet = NonPlanet()
            self.__nonplanets.append(non_planet)
            return non_planet in self.__nonplanets

    def __str__(self):
        return f'This universe has {len(self.__planets)} planets, and {len(self.__nonplanets)} other entities.'

    def display_entity(self) -> None:
        all_entities = self.__planets + self.__nonplanets
        for entity in all_entities:
            print(entity)

    def display_nonplanet(self) -> None:
        for non_planet in self.__nonplanets:
            print(non_planet)


u1 = Universe()

print(u1.__str__())
print(u1.display_entity())