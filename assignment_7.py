# in a program, a dictionary contains lists of students and their courses. The teacher is interested to have a dictionary that has the courses as key and the students enrolled in each course as values. Each key has three different values.

# To address this requirement, write a function to invert the dictionary and implement a solution that satisfies the teacher’s need. In particular, the function will need to turn each of the list items into separate keys in the inverted dictionary. Also provide a technical explanation for the code and its output in minimum 200 words.

# Programming Instructions:
# Print the original dictionary as well as the inverted dictionary.
# Include your the Python program and the output in your submission.
# The code and its output must be explained technically. The explanation can be provided before or after the code, or in the form of comments within the code.

def invert_student_courses(student_courses):
    inverse = dict()

    for student, courses in student_courses.items():
        for course in courses:
            if course not in inverse:
                inverse[course] = []  # Initialize an empty list if the course is not in the dictionary
            inverse[course].append(student)  # Append the student to the course's list

    return inverse

# Sample input
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}


# Invert the student_courses dictionary
inverted_output = invert_student_courses(student_courses)

# Display the results
print(inverted_output)
print('\n', student_courses)

# student_courses =  { 
#    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
#    'Stud2': ['CS2402', 'CS2001', 'CS1102']
#  }

# def invert_dict(student_courses):
#     inverse = {}
#     for student, courses in student_courses.items():
#         for course in courses:
#             if student not in inverse:
#                 inverse[course] = []
            
#             inverse[course].append(student)
           
#     return inverse
       
        
# print(invert_dict(student_courses))
# print('\n', student_courses)