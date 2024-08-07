
# Discussion Assignment
# Welcome to the Unit 7 Discussion Forum!

# Implement your own Python code examples to describe how tuples can be useful with loops over lists and dictionaries. Do not copy code from the textbook or any other source. 

# Your descriptions and examples should include: the zip function, the enumerate function, and the items method. 

# The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, Your answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit from which your colleagues can formulate a response or generate further discussion. Remember to post your initial response as early as possible, preferably by Sunday evening, to allow time for you and your classmates to have a discussion.

# When you use information from a learning resource, such as a textbook, be sure to credit your source and include the URL. Continue to practice using APA format for citations and references.



#.ZIP
# The Zip function combines and pairs two tuples together and returns a single iterable tuple, kind of like a zipper closing in on each other, so one side closes then the next side follows, here one side is represented by the tuple of students and the other is the list of grades (Downey, 2015, pg. 119).

students = ('Ana', 'Joe', 'Frasier')
grades =  [80, 90, 68]

for students, grades in zip(students, grades):
    print(f"{students}: {grades}")

#.ENUMERATE
fruits = ['apple', 'banana', 'orange', 'peach']

for index, element in enumerate(fruits):
    print(index, element)

# enumerate allows you to loop through a list and also retrieve the indexes of each item within the list, each_with_index (Downey, 2015, 119).

#.ITEMS

# Dictionaries have a method called items that returns a sequence of tuples, where each
# tuple is a key-value pair This is useful for iteration when you want to access both keys and their corresponding values (Downey, 2015, 120).

animals_seen = {'koala':0, 'cats':1, 'owls':2}

for key, value in animals_seen.items():
    print(f"animals seen {key} {value}")


# References 




