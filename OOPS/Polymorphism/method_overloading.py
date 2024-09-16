class a:
    def show(self):
        print("Welcome")

    def show(self, fname=''):
        print(f"Welcome {fname} ")

    def show(self, fname='', lname=''):
        print(f"Welcome {fname} {lname} ")


obj = a()
obj.show("Bhushan")
obj.show("Bhushan", "Chaudhari")
