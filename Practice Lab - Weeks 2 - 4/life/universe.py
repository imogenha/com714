from planet import Planet
from planet import NonPlanet
from typing import List

class Universe:

    def __init__(self):
        self.__planets = []
        self.__nonplanets = []

    def generate_planet(self, planet_names: List[str]) -> bool:
        generated_planets = []
        planet = Planet()
        for planet in planet_names:
            self.__planets.append(planet)
            generated_planets.append(planet)
        return planet in generated_planets

    def generate_entity(self, entity_names: List[str]) -> bool:
        generated_entities = []
        entity = NonPlanet
        for entity in entity_names:
            self.__nonplanets.append(entity)
            generated_entities.append(entity)
        return entity in generated_entities

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

print(u1.generate_entity(['E1', 'E2']))
print(u1.__str__())