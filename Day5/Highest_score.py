max = 0
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > max:
    max = student_scores[n]
  else:
    continue
    
print(max)
#print(max(student_scores))

# Ideally if you want to find the max in a list you can just use the max function. You could also set a max accumulator and then use an if function, but when I try to do that it doesnt work for me.
