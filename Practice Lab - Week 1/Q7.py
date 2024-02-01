# Prompt the user to enter a phrase

def box_phrase(phrase, option):
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
        n = int(input("Enter a value: "))
        row = (len(phrase + " ") * n) + 4
        h = ''.join(['+'] + ['-' * row] + ['+'])
        result = h + (('\n'"|" + "  " + ((phrase + " ") * n) + "  " + "|"'\n') * n) + h
        print(result)
