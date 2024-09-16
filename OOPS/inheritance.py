class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print(f"{self.name} {self.surname}")


p = person("Bhushan", "Chaudhari")
p.info()


class people(person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def intro(self):
        print(f"Your age is {self.age}")


p = people("Varun", "Dhawan", 24)
p.intro()
