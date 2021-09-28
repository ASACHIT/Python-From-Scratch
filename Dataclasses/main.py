from dataclasses import dataclass, field

"""Dataclasses let you to quickly build objects that represent data and easily compare, sort, or order them."""

@dataclass(order=True)
class Person:
    """INIT=FALSE to stop initializing as attr, REPR=FALSE to prevent presenting as a string"""
    sort: int = field(init=False, repr=False)
    name: str
    age: int
    location: str
    sex: str
    planet: str = "earth"       # Default value

    """Now Person is data class, so dont need a initialization method"""
    def __post_init__(self):
        self.sort = self.age


person1 = Person(name="bibek", age=21, location="ktm", sex="male")
person2 = Person(name="nerisha", age=20, location="ktm", sex="female")
person3 = Person(name="sachit", age=17, location="chitwan", sex="male")

'''prints data presents in objects'''
print(person1)
print(person2)
print(person3)

"""You can compare 2 objects with data classes"""
print(person1 > person2 > person3)  
''' prints True ,  its sorting by age  sort_index has been set for age'''
