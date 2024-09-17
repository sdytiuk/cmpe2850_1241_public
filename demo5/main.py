#Today's topics:
# args and qwargs
# yield
# list comprehensions
from itertools import count
from pydoc import describe


def greet(*names):
    """
    pass in a list of names and we will greet each one
    :param names: list of names
    :return:
    """
    for name in names:
        print("Hello, " + name + "!")

def describe_person(**attributes):
    for key, value in attributes.items():
        print(key + ": " + str(value))


def countdown(start):
    while start >=0:
        yield start
        start -= 1

def simpleYield():
    yield 1
    yield 2


def word_frequency(sentence):
    words = sentence.split()
    word_count = {word: words.count(word) for word in words}
    return word_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    classmembers = ('Ben', 'Vidal', 'Anna')
    greet('Ben', 'Vidal', 'Anna')

    describe_person(name="Alice", age=30, city="New York")

    person_dict = {"55":"Alice", "age":30, 'city':"New York"}

    describe_person(**person_dict)

    print(str(countdown(10)))

    for number in countdown(10):
        print(number)

    print(simpleYield())

    for num in range(10):
        for result in simpleYield():
            print(result)

    #squaring numbers with list comprehension
    numbers = (1,2,3,4,5,6)
    squares = [num**2 for num in numbers if num%2 == 0]
    for square in (num**2 for num in numbers if num%2 == 0):
        print(square)
    print(squares)

    #list comp with dictionary output
    print(word_frequency("the brown dog jumped the fence"))

    print(word_frequency("Did you ever hear the tragedy of Darth Plagueis the wise? No. I thought not, It's No story the jedi would tell you. It's a sith legend. Darth Plagueis was a Dark Lord of the sith. He was so powerful, Yet so wise. He could use the force to influence the medi chlorians to create, Life. He had such a knowledge of the Dark side, He could even keep the ones he cared about, From dying. He could actually, Save the ones he cared about from death? The dark side of the force is a pathway to many abilities some consider to be unnatural. Well what happened to him? Darth Plagueis became so powerful that the only thing he feared was losing his power, Which eventually of course he did. Unfortunately, He taught his apprentice everything he knew. Then his apprentice killed him in his sleep. Ironic, He could save others from death, But not himself. Is it possible to learn this power? Not from a jedi."))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
