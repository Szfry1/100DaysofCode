# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
# "Function": "A piece of code that you can easily call over and over again."
# }

# print(programming_dictionary["Bug"])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
 
for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] < 101:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
        
print(student_scores)
print(student_grades)

    # print(student_scores[key])
    # student_scores[key] = "This is string"
    # print(student_scores[key])   
    # print(student_scores)
      


#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
# print(student_grades)
