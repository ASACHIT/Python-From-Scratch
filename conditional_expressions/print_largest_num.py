"""Program to print the largest number from four numbers entered by users."""

num1 = int(input("Input 1st number: "))
num2 = int(input("Input 2st number: "))
num3 = int(input("Input 3st number: "))
num4 = int(input("Input 4st number: "))
if num1 > num2 or num3 or num4:
    print(f"{num1} is Largest Number Among 4")
elif num2 > num1 or num2 or num3:
    print(f"{num2} is Largest Number Among 4")
elif num3 > num1 or num2 or num4:
    print(f"{num3} is Largest Number Among 4")
else:
    print(f"{num4} is largest number among 4 ")
