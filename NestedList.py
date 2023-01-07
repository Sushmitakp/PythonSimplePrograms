import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lst=[rock,paper,scissors]
user_input=int(input("What did you choose? Type 0 for Rock,1 for Paper or 2 for scissors"))
print(lst[user_input])

random_selection=random.randint(0,2)
print(f"Computer choose:{random_selection}")
print(lst[random_selection])

if user_input >=3 or user_input<0:
  print("Its an invalid number")
  exit()
  print(lst[user_input])

row1=[0,1,2]
row2=[2,0,1]
row3=[1,2,0]
map=[row1,row2,row3]

result=map[random_selection][user_input]

if result == 0:
  print("Its a draw")
elif result == 1:
  print("You won")
elif result == 2:
  print("You lose")

