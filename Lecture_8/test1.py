class Student:
    country = "Israel"
    def __init__(self, name, age, department, startYear):
        self.name = name
        self.age = age
        self.department = department
        self.startYear = startYear


def main():
    s = Student("Israel Israeli", 20, "sw", 2023)

    print(f"Student Name: {s.name}, Year: {s.startYear}")

main()