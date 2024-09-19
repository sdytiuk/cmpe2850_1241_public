# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add(x, y):
    """
    Adds two numbers.
    Anything you want to say.
    Say it here.
    >>> add(2,3)
    5
    >>> add(-1,4)
    3

    :param x:
    :param y:
    :return:
    """
    return x + y

def AddAll(*args):
    """

    :param args: any number of ints to add
    :return:
    """
    accumulator = 0
    for arg in args:
        accumulator += arg
    return accumulator


def apply_operation(x, operation):
    return operation(x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(add(2,3))
    import doctest
    doctest.testmod()

    #lambda time
    my_list = [(1,2), (3,1), (2,3)]
    #sort by the second element of each tuple
    sorted_list = sorted(my_list, key=lambda x: x[1])

    print(sorted_list)

    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)

    squared_numbers = list(map(lambda x: x**2, numbers))
    print(squared_numbers)

    result = apply_operation(5, lambda x: x * 2)
    print(result)

    print(AddAll(1,2,3))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
