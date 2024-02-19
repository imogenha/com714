from clothingsize import ClothingSize


class Clothing:

    def __init__(self, colour: str, material: str, size: ClothingSize):
        self.__colour = colour
        self.__material = material
        self.__size = size

    def repr(self):
        return f'clothing (colour= {self.__colour}, material= {self.__material}, size= {self.__size})'

    def str(self):
        return f'This clothing item is made from {self.__material}, is {self.__colour} and is {self.__size} in size'

    def dye(self, new_colour) -> bool:
        self.__colour = new_colour
        print(new_colour)
        return new_colour in self.__colour

    def gain_weight(self):
        if self.__size == 5:
            print("Cannot gain any more weight!")

        else:
            self.__size = ClothingSize(self.__size + 1)
            print(self.__size)
            return self.__size

    def loose_weight(self):
        if self.__size == 1:
            print("Cannot lose any more weight!")

        else:
            self.__size = ClothingSize(self.__size - 1)
            print(self.__size)
            return self.__size
