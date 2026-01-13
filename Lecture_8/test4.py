class Student:
    country = "Israel"
    def __init__(self, name, age, country, department, startYear):
        self.name = name
        self.age = age
        self.age = country
        self.department = department
        self.startYear = startYear
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def satisfaction(self, satisfaction):
        return f"{self.name} is studying on {self.department} and they are {satisfaction}"

def main():
    s = Student("Charlie Kirk", 23, "Israel", "Software Engineer", 1994)

    print(f"Description: {s.description()},\nSatisfaction Level: {s.satisfaction("very satisfied!")}")

main()