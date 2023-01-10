#Program to find the sum of even numbers from 1 to 100 using Range function
total=0
for number in range(2,101):
    if number%2==0:
        print(number)
        total+=number
print(total)