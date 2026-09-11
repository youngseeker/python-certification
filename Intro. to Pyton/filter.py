words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print("Long words (more than 4 letters):", long_words)
short_words = list(filter(lambda w: len(w) <= 4, words))
print("Short words (4 letters or fewer):", short_words)

# This code defines a list of words and uses the filter() function
# to create two new lists: one with words longer than 4 letters
# and another with words of 4 letters or fewer. It demonstrates
# the use of both a named function and a lambda function with filter().

# map function example
uppercased_words = list(map(str.upper, words))
print("Uppercased words:", uppercased_words)
# This code uses the map() function to convert all words in the list
# to uppercase and prints the resulting list.
# another map() example
celcius_temperatures = [0, 10, 20, 30, 40, 50]
fahrenheit_temperatures = list(map(lambda c: (c * 9/5) + 32, celcius_temperatures))
print("Fahrenheit temperatures:", fahrenheit_temperatures)
# This code converts a list of temperatures from Celsius to Fahrenheit
# using the map() function along with a lambda function.
celcius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celcius))
print(fahrenheit)

# sum function example
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum of numbers:", total)
# This code calculates the sum of a list of numbers using the sum() function
# and prints the result.

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10)
print("Sum of numbers with a starting value of 10:", total)
# This code calculates the sum of a list of numbers using the sum() function
# with a specified starting value and prints the result.

# lambda function example
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4
    
print(calculate_expression(3))  # Output: 14
print(calculate_expression(-2)) # Output: 10