from human import Human
from planet import Planet


class Universe:

    def __init__(self):
        self.__planets = []

    def generate(self) -> bool:
        planet = Planet()
        self.__planets.append(planet)
        return planet in self.__planets

    def display(self) -> None:
        for planet in self.__planets:
            print(planet)


U1 = Universe()


print(U1.generate())
print(U1.display())

