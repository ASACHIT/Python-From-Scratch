class Student:
    def __init__(self, name, cls, roll):
        self.name = name
        self.cls = cls
        self.roll = roll


class Result(Student):
    def __init__(self, name, cls, roll, english, math, science, computer):
        super().__init__(name, cls, roll)
        self.eng = english
        self.mth = math
        self.science = science
        self.comp = computer

    def result(self):
        print(
            f"""
         {'='*20} Result of {self.name} {'='*20}
                    Student Name - {self.name}
                    class        - {self.cls}
                    Roll Number  - {self.roll}
        {'-'*21} Marks In Subjects {'-'*21}

                    English      -  {self.eng}
                    Math         -  {self.mth}
                    Science      -  {self.science}
                    computer     -  {self.comp}


        """
        )


sachit = Result(
    name="sachit", cls="11", roll="10", english=80, math=60, science=70, computer=90
)
nishant_sapkota = Result(
    name="nishant Sapkota",
    cls="10",
    roll="1",
    english=80,
    math=90,
    science=90,
    computer=99,
)
bibek_subedi = Result(
    name="bibek subedi",
    cls="10",
    roll="1",
    english=99,
    math=99,
    science=89,
    computer=98,
)
nishant_sapkota.result()
bibek_subedi.result()
sachit.result()


"""multiple inheritance"""


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
