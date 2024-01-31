# Prompt the user to enter a phrase

def box_phrase():
    phrase = input("Enter a Phrase: ")
    option = int(input("Enter a choice between 1-4: "))
    padding = len(phrase) + 1
    row = len(phrase) + 4
    h = ''.join(['+'] + ['-' * row] + ['+'])

    if option == 1:
        result = h + '\n'"|" + "  " + phrase + "  " + "|"'\n' + h
        print(result)

    elif option == 2:
        result = '\n' + (' ' * padding) + h + '\n' + phrase + " " + "|" + (' ' * row) + "|"'\n' + (' ' * padding) + h
        print(result)

    elif option == 3:
        result = '\n' + h + '\n' + "|" + (' ' * row) + "|" + " " + phrase + '\n' + h
        print(result)

    elif option == 4:
        define_n = int(input("Enter a value: "))


box_phrase()


# Option 1: display a box with a phrase inside it.

# Option 2: Display a box to the right of the phrase.

# Option 3: Display a box to the left of the phrase.

# Option 4: Display a box that is n x n.