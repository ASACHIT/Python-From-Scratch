"""
python list is the container that stores a list of values with different data types
"""
list = ["python", "ITSNP", "Sachit", "Django", "8080"]

print(list[0])  # prints first value from list (python)
print(list[1])  # prints second value from list (ITSNP)
print(
    list[0:3]
)  # prints all values index starting with 0 to 3 (python...to... Sachit) string slicing


# LIST METHODS
list.sort()  # it sort values in list
list.append(5050)  # add given value at the end of the list
print(list)


list.insert(0, "firstvalue")  # add "firstvalue" to index 0 in the list
print(list)


list.pop()  # its removes last value from list by default
print(list)

list.pop(0)  # it will remove value which is in index 0 (firsvalue)
print(list)


list.remove("python")  # .remove('value') will remove 'python' from list
print(list)
