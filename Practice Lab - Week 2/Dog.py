class Dog:
    def bark(self):
        print("bark bark!")

    def __init__(self, name, age, species):
        self.name = name
        self.age = int(age)
        self.species = species


puppy1 = Dog("Sushi", 4, "Husky")

print(puppy1.name)
print(puppy1.age)
print(puppy1.species)
print(puppy1.bark())