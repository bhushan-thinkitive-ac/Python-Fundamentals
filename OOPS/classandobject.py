class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Name: {self.name}, Age: {self.age}")


p = person("Bhushan", 24)
p.intro()
