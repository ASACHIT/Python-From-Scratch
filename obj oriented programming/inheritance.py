"""
inheritance in Object oriented programming
single inheritance
"""


class Detail:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


class Info(Detail):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


aboutme = Detail("myname", "int", "somewhere")
print(
    f"Hi, My Name is {aboutme.name}  age- {aboutme.age} currently living in {aboutme.location}"
)


"""Multiple Inheritance"""


class parent:
    X = "hi i am from 'parent' class "


class secondparent:
    Y = "Hi i am from 'secondparent' class"


class child(parent, secondparent):
    Z = "Hi i am from 'Child' class"


Child = child()
print(Child.X)
print(Child.Y)
print(Child.Z)
