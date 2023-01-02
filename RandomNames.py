#To generate a random name and pick the name from the list and user is goign to pay the bill
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length=len(names)
#Random name to pick and pay the bill
v=random.randint(0,length-1)
print(f'{names[v]} is going to buy the meal today!')




