from new import Student
import new
# Word replacement program


sentence = input("Enter your sentence: ")
print(f"Your sentence is: {sentence}")
word1 = input("Enter the word to replace ")
word2 = input("Enter the word to replace it with ")
print(sentence.replace(word1, word2))

# Lists in Python
countries = ["United Kingdom", 'Ghana', 'Nigeria',
             'Australia']
print(type(countries))
# Tuples in Python: tuples are immutable
# They can't be changed
numbers = (6, 4, 3, 5, 3)
strings = ("Hello", "You there")
print(strings)
print(numbers)
# Functions in Python
# Functions are bunch of codes which perform a
# particular task
# The allow u package your code well



def greetings_function(name, age):
    print(f"Welcome {name}, you are {age} years old")


greetings_function("Kelvin", 34)


def users_name(*names):
    print(f"Welcome {names[1]}")


users_name("Bro", "Sis", "Hey")


# Return Statements
# They are being used to get a response from the task
# being executed in a function


def my_function():
    return 5 + 4


def add_numbers(num1, num2):
    return num1 + num2


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))


print(add_numbers(num1, num2))


value = input("Enter a value: ")

if value < str(10):
    print(f"{value} is less than 10")
else:
    print(f"{value} is more than 10")

# Building  a python program to check
# if a number is an even number
number = int(input("Enter a number "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

i = 1
while i < 6 or i == 6:
    print(i)
    i += 1
for letter in "Hello":
    print(letter)
my_list = ["he", "she", "they", "them"]
for values in my_list:
    if values == "they":
        break
    print(values)
# Try Exceptions in Python
try:
    x = int(input("Input an Integer: "))
    print(x)

except ValueError:
    print("Something went wrong... Please try again")
finally:
    print("Try except finished")
# Classes and objects in Python


class Person(Student):
    pass


p1 = Person()
print(p1.name)

new.say_hi()
# Introduction to Pip
# Pip is used for installing external modules/packages from the web to the local PC
# Pip allows u to install modules from the internet to the laptop
# Django is a web framework which allows you to build website using Python
