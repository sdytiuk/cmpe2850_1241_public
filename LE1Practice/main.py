


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Exercise 1: List Comprehension for Squaring Even Numbers

    Prompt: Create a new list containing the squares of even numbers from a given list.

    Python"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squared_even = [num ** 2 for num in numbers if num % 2 == 0]

    print(squared_even)  # Output: [4, 16, 36, 64, 100]

    """
    Exercise 2: Dictionary Comprehension for Word Counts

    Prompt: Create a dictionary where the keys are words from a given 
    sentence and the values are their corresponding counts.
    """
    sentence = "the quick brown fox jumps over the lazy dog"

    word_counts = {word: sentence.count(word) for word in sentence.split()}
    print(word_counts)

    # Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

    """
    Exercise 3: Set Comprehension for Unique Characters

    Prompt: Create a set containing unique characters from a given string.
    """
    string = "hello world"

    # unique_chars = set(string)
    unique_chars = { c for c in string}

    print(unique_chars)  # Output: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

    """
    Nested Comprehension Example: Creating a Matrix
    Prompt: Create a 3x3 matrix where each element is the 
    product of its row and column indices.
    """
    rows, cols = 3, 3
    matrix = [[i * j for j in range(cols)] for i in range(rows)]
    print(matrix) # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

    """
    Exercise 1: Fibonacci Sequence Generator
    Prompt: Create a generator that produces the Fibonacci sequence, which starts with 0 and 1, 
    and each subsequent number is the sum of the previous two.
    """


    def fibonacci_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b


    # Example usage:
    fib_gen = fibonacci_generator()
    for i in range(10):
        print(next(fib_gen))

    """
    Exercise 2: Prime Number Generator
    Prompt: Create a generator that produces prime numbers.
    """
    def prime_generator():
        num = 0
        while True:
            num += 1
            if len([x for x in range(num) if (num / (x+1)).is_integer()]) < 3:
                yield num

    # Example usage:
    prime_gen = prime_generator()
    for i in range(10):
        print(next(prime_gen))

    """
    Exercise 1: Reverse String

    Prompt: Reverse a string using a loop and negative indexing.
    """
    def reverse_string(string):
        reversed_string = ""
        #is this actually negative indexing???
        for i in range(-1, -len(string) - 1, -1):
            reversed_string += string[i]
        return reversed_string

    # Example usage:
    string = "hello world"
    reversed_string = reverse_string(string)
    print(reversed_string)
    # Output: "dlrow olleh"

    """
    Exercise 1: Divide by Zero Handling
    Prompt: Write a function that divides two numbers. Handle the ZeroDivisionError exception and 
    return a custom message indicating that division by zero is not allowed.
    """


    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        return result

    # Example usage:
    result = divide_numbers(10, 2)
    print(result)  # Output: 5.0

    result = divide_numbers(10, 0)
    print(result)  # Output: Error: Division by zero is not allowed.