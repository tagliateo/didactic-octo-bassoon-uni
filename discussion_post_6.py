
# Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.

# Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

# Create your own unique examples for this assignment.
#
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(list1 == list2) # expected to return true

print(list1 is list2) # expected to return False

list3 = list1

print(list3 is list1) # expected True

# In programming, especially in Python, it is important to understand the distinction between two terms: "equivalent" and "identical".

#     Equivalent: Two objects or values are considered equivalent if they look the same or if they hold the same value, even if they are two separate entities in memory.
#     Identical: Two objects are identical if they refer to the exact same object in memory. In Python, this is checked using the is operator.

# Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references.
#
original_list = [1,2,3,'a']

def lister(original_list):
    new_list = original_list.append(900)
    print("new list:", new_list)
    print(original_list)



print(lister(original_list))

# original_list is being passed into our function as an argument
# a new reference is being created in that is referencing the parameter original_list and then the parameter is being modified by appending the integer 900 to the list
# the list is then being printed so we can inspect
