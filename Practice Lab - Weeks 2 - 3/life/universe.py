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

    def display_planet(self) -> None:
        for planet in self.__planets:
            print(planet)

    def display_nonplanet(self) -> None:
        for non_planet in self.__nonplanets:
            print(non_planet)



