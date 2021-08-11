student_heights = input("Input a list of student heights ").split()
average_sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(n)
  average_sum += student_heights[n]  

print(average_sum)
print(len(student_heights))  
full_average = average_sum / len(student_heights)

print(round(full_average))

# generally you could use the sum function but it was specifically asked to not use that function. I actually had to think about this for a second. I kept putting average_sum += n 
# which wasn't actually specifying anything I need to have student_heights[n]


