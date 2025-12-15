class Student:
    country = "Israel"
    def __init__(self, name, age, department, startYear):
        self.name = name
        self.age = age
        self.department = department
        self.startYear = startYear

def main():
    Std1 = Student("Israel Israeli", 20, "sw", 2023)
    Std2 = Student("Israel Israeli", 25, "sw", 2023)
    isEqual = (Std1.age==Std2.age)
    print(isEqual)

main()