# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_bye(name : int) :
    """
    This function prints a goodbye message to the person
    :param name: The name of the person to say bye to
    :return: the message to display
    """
    print(type(name))
    return f'Bye, {name}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Zach')
    print(print_bye(9))
    print(print_bye('summer'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
