student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)

#Substitute for Max function()
students=student_scores[0]
for highest_score in student_scores:
  if highest_score > students:
    students=highest_score
print(f"The highest score in the class is:{students}")

#Substitute for Min function()
students = student_scores[0]
for student_score in student_scores:
  if student_score < students:
    students = student_score
print(f"The lowest score in the class is :{students}")