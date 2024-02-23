from living_thing import LivingThing


class Planet:
    def __init__(self, name: str = ''):
        self.__name = name
        self.__living_things = []

    def __repr__(self):
        return f'Planet(Name = {self.__name}, Living Things = {self.__living_things.__repr__()})'

    def __str__(self):
        return f'Planet {self.__name} has {self.__living_things} living things.'

    def add(self, form: LivingThing) -> bool:
        self.__living_things.append(form)
        return form in self.__living_things

    def remove(self, form: LivingThing) -> bool:
        self.__living_things.remove(form)
        return form in self.__living_things

    def has(self, form: LivingThing) -> bool:
        return form in self.__living_things

    def population(self):
        return len(self.__living_things)


class NonPlanet:

    def __init__(self, name: str = ''):
        self.__name = name
        self.__living_things = []

    def population(self):
        return len(self.__living_things)