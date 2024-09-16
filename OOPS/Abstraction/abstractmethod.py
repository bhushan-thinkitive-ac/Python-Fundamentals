from abc import ABC, abstractmethod


class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")

    @abstractmethod
    def speed(self):
        pass


class maruti(Car):
    def speed(self):
        print("The speed of maruti is 100km/hr ")


class suzuki(Car):
    def speed(self):
        print("The speed of maruti is 50km/hr ")


obj = maruti()
obj.show()
obj.speed()

obj2 = suzuki()
obj2.show()
obj2.speed()
