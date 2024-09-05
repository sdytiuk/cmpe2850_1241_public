"""
Demo for menus and ICA01
Steven Dytiuk
Sept 5, 2024
"""


def displayMenu():

    default = 100

    userinput = input(f'Enter your favourite number [{default}]') or default
    return userinput

def menu(items, default):
    todaysSpecial = default
    for item in items:
        print(f'{item[0]}: {item[1]}')
    response = input('Selection: ' + '[' + default + ']') or default
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #selection = displayMenu()
    #print(f'The user selected {selection}')

    items = (('A', 'Apple Pie'), ('B', 'Coffee'), ('C', 'Banana'))

    choice = menu(items, 'B')

    print(choice)

    print("Negative indexing feature!!")
    print(items[-5])


