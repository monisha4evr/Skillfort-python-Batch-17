from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand):
        self.brand=brand

    @abstractmethod
    def sample(self):
        pass
       # print("Sample in Abstract")

    @abstractmethod
    def display(self):
        pass

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def display(self):
        print(self.brand)

c=Car("maruthi")
c.display()
c.sample()


----------------

from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def bark():
        pass

class Dog(Animal):
    def bark(self):
        print("Woof")

class Cat(Animal):
    def bark(self):
        print ("Meow")

d=Dog()
d.bark()

c=Cat()
c.bark()

----------------

class Test:
    def sample(self):
        print("Hello")

class Welcome(Test):
    def sample(self):
        #super().sample()
        print("Welcome")

w=Welcome()
w.sample()

class Test:
    def add(self,x,y,z=None,w=5):
        if z :
            print(x*y*z*w)
        else:
            print(x,y,z,w)


t=Test()
t.add(1,2)
t.add(1,2,3)
t.add(1,2,3,7)

class Test:
    def __init__(self,username,cust_number,password):
        self.username=username
        self._number=cust_number
        self.__password=password

    def get_password(self):
        print("Password",self.__password)

    
t=Test("monisha",12345,'mm@123')
print(t.username)
print(t._number)
t.get_password()
print(t._Test__password)


class Grandparent:
    def __init__(self):
        print("parent")

class Parent1(Grandparent):
    def __init__(self):
        super().__init__()
        print("Child1")

class Parent2(Grandparent):
    def __init__(self):
        super().__init__()
        print("Child2")

class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
        print("Child")

c=Child()
print(Child.__mro__)

    


