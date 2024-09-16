class A:
    _a = 10
    __b = 20

    def show(self):
        print("A= ", self._a, "B= ", self.__b)

    def displayPrivatedata(self):
        self.__b()


obj = A()
obj.show()

print("The value of A is ", obj._a)


try:
    print("The value of B is ", obj.__b)
except AttributeError as e:
    print("The variable is protected and cannot be accessed outside the class ", e)
