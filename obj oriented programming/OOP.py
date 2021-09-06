class Info:
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

    def aboutme(self):
        print(
            f"""My Name Is {self.name}\nI Am From {self.location}\nAge- {self.age}
         """
        )


me = Info("sachit", "bharatpur", "17")  # instance attribute !
me.aboutme()
unknown = Info("noname", "earth", "null")
unknown.aboutme()


# Static Method
class Test:
    @staticmethod  # decorator to mark function as a static method
    def dosomething():
        print("Doing Something...")


Test.dosomething()
