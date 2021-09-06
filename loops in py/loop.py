"""Creates 10 text file and write multiplication table serially from 1 to 10"""
# For loop
def mult():
    for numbers in range(1, 11):
        f = open(f"{numbers}.txt", "w")
        for i in range(1, 11):
            data = f"{numbers}x{i}={numbers*i}\n"
            f.write(data)
        print(f"{numbers}.txt created with multiplcation table of {numbers}")


mult()


# while loop
"""Takes a number as an input and print its multiplication table"""


def multiplication_table(number):
    num = 1
    # while loop
    while num <= 10:
        print(f"{number} x {num}=", number * num)
        num += 1


multiplication_table(int(input("Input a Number: ")))
