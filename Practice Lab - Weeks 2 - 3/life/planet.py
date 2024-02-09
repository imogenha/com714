from human import Human


class Planet:
    def __init__(self, name: str = ''):
        self.__name = name
        self.__humans = []

    def __repr__(self):
        return f'Planet(Name = {self.__name}, Humans = {self.__humans.__repr__()})'

    def __str__(self):
        return f'Planet {self.__name} has {self.__humans} humans.'

    def add(self, human: Human) -> bool:
        self.__humans.append(human)
        return human in self.__humans

    def remove(self, human: Human) -> bool:
        self.__humans.remove(human)
        return human in self.__humans

    def has(self, human: Human) -> bool:
        return human in self.__humans

    def population(self):
        return len(self.__humans)


class NonPlanet:

    def __init__(self, name: str = ''):
        self.__name = name
        self.__humans = []

    def population(self):
        return len(self.__humans)