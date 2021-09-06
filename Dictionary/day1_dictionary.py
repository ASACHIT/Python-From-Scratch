"""Dictionaries is collection of keyvalue pairs.it is ordered and changeable but it doesnot allow duplicates values.."""

dictionary = {
    "python": "Python is an interpreted high-level general-purpose programming language.",
    "django": "Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern",
    "flask": "Flask is a micro web framework written in Python.",
}

for key, value in dictionary.items():  # .items() return a list of key & values tuples
    print(key, ":", value)
    print(
        dictionary.keys()
    )  # .keys() will return and prints keys only from dictionary !


# .update() will update values in dictionary
dictionary.update(
    {
        "django": "Django is a python based webframework that follow MVT architectural pattern"
    }
)
# value of django is updated now !


""".get() returns values of specifed keys but if given value is not present in dictionary it will return none
whereas | dictionary.["keyname"] | throws an error if key is not present in dictionary"""

# print(dictionary["notindict"])   #it will throw an error because key is not present in dictionary

print(dictionary.get("django"))  # prints value of given keys name (django)
print(dictionary.get("flask"))  # prints value of given keys name (flask)
print(dictionary.get("python"))  # prints value of given keys name (python)
