# This assignment will assess your skills and knowledge in developing a function through an incremental development process such that the debugging becomes fast. There are two parts of this assignment, and you must submit both parts.

# Part 1
# You work as a software developer in a company that creates custom software solutions for various clients. Your company has been approached by an educational client who wants to develop a function that calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments. Your manager has instructed you to use incremental development to create the necessary function and document each stage of the development process. After completing the final stage of development, you have to test the function with different arguments and record the outputs in your Learning Journal.


#Stage 1: Planning

#Problem definition: The client wants a function that calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.
 #Requirements: The function should take two arguments (the lengths of the legs) and return the length of the hypotenuse.

 #Design: We will use the Pythagorean theorem to calculate the length of the hypotenuse.

#Stage 2: Code Development

 #Start by importing the math module, which contains the sqrt function, which we will use to calculate the square root.

import math

 # Define the function `hypotenuse` with two arguments `a` and `b`, representing the lengths of the legs.

def hypotenuse(a, b):
    pass

# Calculate the sum of the squares of `a` and `b`.

c = math.sqrt(a**2 + b**2)

# Return the result as a float value.
return c

# The final code for this stage is:

import math

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Stage 3: Testing

# Test the function with different sets of input values to ensure it works correctly.

print(hypotenuse(3, 4))  # expected output: 5.0
print(hypotenuse(5, 12))  # expected output: 13.0
print(hypotenuse(1, 1))  # expected output: √2.0 (approximately 1.4142135623730951)

# All tests pass!

#Stage 4: Finalization

# Add docstrings to document the function and its parameters.

def hypotenuse(a: float, b: float) -> float:
    """
    Calculate the length of the hypotenuse of a right triangle given the lengths of the other two legs.

    Args:
        a (float): The length of one leg.
        b (float): The length of the other leg.

    Returns:
        float: The length of the hypotenuse.
    """
    c = math.sqrt(a**2 + b**2)
    return c

# The final code is complete

#Learning Journal Entry

 #Date: [Insert Date]
 #Function Developed: `hypotenuse`
 #Description: The `hypotenuse` function calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.
 #Testing Results:
	# + `hypotenuse(3, 4)` returned 5.0 (expected)
	# + `hypotenuse(5, 12)` returned 13.0 (expected)
	# + `hypotenuse(1, 1)` returned approximately 1.4142135623730951 (expected)
 # Reflection: The incremental development process allowed us to break down the problem into smaller stages, making it easier to test and debug each step. The final function works correctly and is well-documented.

# Tasks

# Include all of the following in your submission:

#  An explanation of each stage of development, including code and any test input and output.
#  The output of hypotenuse(3,4).
#  The output of two additional calls to hypotenuse with different arguments.


# Part 2
#  You are a software developer who wants to establish yourself as a skilled and versatile programmer. To achieve this, you have decided to create a work portfolio that showcases your ability to develop custom software solutions. This portfolio will be your gateway to attract potential clients and establish yourself as a freelancer.
# As part of your portfolio, you plan to create your own function that does some useful computation using an incremental development approach that will demonstrate your programming skills and problem-solving abilities. You will document each stage of the development process, including the code and any test input and output in your Programming Assignment.
