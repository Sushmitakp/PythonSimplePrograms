#Program to display the FizzBuzz Game
for i in range(1,101):
    #Divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #Divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    #Divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    print(i)