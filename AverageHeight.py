#Program to check the Average height of students
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#Substitute for Sum function()
total_height=0
for height in student_heights:
 total_height+=height
print(total_height)

#substitute for Len function()
number_of_students=0
for students in student_heights:
    number_of_students+=1
print(number_of_students)

result=round(total_height/number_of_students)
print(result)


