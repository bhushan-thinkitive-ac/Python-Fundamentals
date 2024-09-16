class A:
    def show(self):
        print("this is parent class")


class B(A):
    def show(self):
        super().show()
        print("this is child class")


obj = B()
obj.show()
