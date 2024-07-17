# This assignment will assess your skills and knowledge in developing a function through an incremental development process such that the debugging becomes fast. There are two parts of this assignment, and you must submit both parts.

# Part 1
# You work as a software developer in a company that creates custom software solutions for various clients. Your company has been approached by an educational client who wants to develop a function that calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments. Your manager has instructed you to use incremental development to create the necessary function and document each stage of the development process. After completing the final stage of development, you have to test the function with different arguments and record the outputs in your Learning Journal.

import math

def hypotenuse(a, b):
    sqrd = a**2 + b**2
    c = math.sqrt(sqrd)

    return c


print(hypotenuse(3, 4))  # expected output: 5.0
print(hypotenuse(5, 12))  # expected output: 13.0
print(hypotenuse(1, 1))  # expected output: √2.0 (approximately 1.4142135623730951)

print('PART TWO\n')




# Part 2
#  You are a software developer who wants to establish yourself as a skilled and versatile programmer. To achieve this, you have decided to create a work portfolio that showcases your ability to develop custom software solutions. This portfolio will be your gateway to attract potential clients and establish yourself as a freelancer.
# As part of your portfolio, you plan to create your own function that does some useful computation using an incremental development approach that will demonstrate your programming skills and problem-solving abilities. You will document each stage of the development process, including the code and any test input and output in your Programming Assignment.

def averages(num1, num2):
    avg = int(num1 + num2 / 2)
    return avg

print(averages(4, 4))
print(averages(3, 9))
print(averages(10, 500))
