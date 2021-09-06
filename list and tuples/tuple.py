"""
TUPLE IS AN ORDERED AND UNCHANGE ABLE VARIABLE WHICH CAN STORE MULTIPLE ITEM,VALUES IN IT.
it cannot be manupulated..it is immutable !!
"""

tup = (0, 9, 18, 27, 36, 45)
print(tup)


# !! Important
tuple2 = 80  # this is variable
print(type(tuple2))  # checking its data type

tuple2 = (80,)  # BUT this is a Tuple
print(type(tuple2))  # checking its data type

"""
always put a comma to every single item in a tuple, else python treats it as a variable!
"""

q = (10, 200, 10, 300, 400, 300)
print(q.count(10))  # prints number of repetition of provided value in tuple


S = (20, 10, 30, 50)
print(
    S.index(10)
)  # .index() will return index number of first occurance of 10 in tuple named S
