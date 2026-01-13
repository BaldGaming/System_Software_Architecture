class Student:
    def __init__(self, name, age, startYear):
        self.name = name
        self.age = age
        self.startYear = startYear

    def description(self):
        return f"{self.name} is {self.age} years old"


class SoftwareStudent (Student):    
    def dept(self):
        return f"{self.name} is studying at Software Engineering department."

class MathematicsStudent (Student):    
    def dept(self):
        return f"{self.name} is studying at MAthematics department."
    
class CivilStudent (Student):    
    def dept(self):
        return f"{self.name} is studying at Civil Engineering department."


def main():
    Kirk = SoftwareStudent("Charlie Kirk", 23, 1994)
    Mario = MathematicsStudent("SUUUUPER MAAAARIO", 90, "???")
    Joe = CivilStudent("Joe Biden", 1, 2056)

    for i in (Kirk, Mario, Joe):
        print(i.dept())

main()