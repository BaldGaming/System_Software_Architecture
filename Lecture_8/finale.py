class Dog:
    species = "small dogs"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        print(f"{self.name} is {self.age} years old, and makes the noise {sound}")


class JackRussel (Dog):    
    def make_sound(self):
        return '"Arf"'

class Poodle (Dog):    
    def make_sound(self):
        return '"Grrr"'


def main():
    miles = JackRussel("Miles", 4)
    buddy = Poodle("Buddy", 7)

    for i in (miles, buddy):
        i.speak(i.make_sound())

main()