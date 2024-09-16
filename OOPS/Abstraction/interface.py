from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def show(self):
        pass


class square(shape):
    def show(self):
        print("This is a square")


class circle(shape):
    def show(self):
        print("This is a circle")


s = square()
s.show()

c = circle()
c.show()
