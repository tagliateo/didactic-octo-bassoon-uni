# By the end of this assignment, you will be able to perform addition, deletion, and sorting on the elements of the list as well shall be able to experiment list and related operators

# (a). Consider that you are working as Data Analyst in an organization. The HR department needs you to carry out following operation on existing list of 10 employees name (you can assume 10 names in a list here).
employees = ["Anthony", "Teo", "Zeeshan", "Katy", "Kait", "Karl", "Figma", "Gojira", "Tom Hanks", "Tim Apple"]
#     Split the list into two sub-list namely subList1 and subList2, each containing 5 names.
sublist1 = employees[:5]
sublist2 = employees[5:]

print(sublist1)
print(sublist2)

#     A new employee (assume the name “Kriti Brown”) joins, and you must add that name in subList2.
sublist2.append("Kriti Brown")
print(sublist2)
#     Remove the second employee's name from subList1.

del sublist1[1]
print(sublist1)

#     Merge both the lists.
sublist1.extend(sublist2)
print(sublist1)

#     Assume there is another list salaryList that stores salary of these employees. Give a raise of 4% to every employee and update the salaryList.
salary_list = [45000.50, 61000.75, 72000.00, 50000.20, 55000.60, 48000.90, 83000.40, 92000.10, 67000.30, 75000.95]
print(salary_list)

# Applying a 4% raise
for i in range(len(salary_list)):
    salary_list[i] = salary_list[i] * 1.04
# salary_list = [salary * 1.04 for salary in salary_list]
print(salary_list)
#     Sort the SalaryList and show top 3 salaries.

salary_list.sort()
top_salaries = salary_list[-3:]
print(top_salaries)


# (b). Design a program such that it converts a sentence into wordlist. Reverse the wordlist then. Write the code and output for the same.

input = "Did you ever hear the Tragedy of Darth Plagueis the Wise?"
print(input)
newer_list = input.split()
print(newer_list)
reverse = newer_list[::-1]
print(reverse)
delimitter = ' '
reversed_list = delimitter.join(reverse)
print(reversed_list)
