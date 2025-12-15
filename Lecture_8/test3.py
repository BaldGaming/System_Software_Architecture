class Student:
    country = "Israel"
    def __init__(self, name, age, country, department, startYear):
        self.name = name
        self.age = age
        self.age = country
        self.department = department
        self.startYear = startYear

def main():
    Kirk = Student("Charlie Kirk", 23, "Israel", "Software Engineer", 1994)
    Mario = Student("SUPER MARIO!!!!", 90, "Pakistan", "Dirt Collector", 2027)
    Joe = Student("Joe", -16, "Thailand", "Shit Inspector", "????")

    for i in (Kirk, Mario, Joe):
        print(f"Student Name: {i.name}, Age: {i.startYear}, Country: {i.country}, Department: {i.department}, Year Started: {i.startYear}")

main()