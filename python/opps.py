# class= > Blueprint
# object => instance of class
# method => function

# types : 3
#     1. instance method  self
#     2. class method
#     3. static method 

class Sample:
    def welcome(self):
        print("Welcome")

s=Sample()
s.welcome()


class Sample:
    def welcome(self,a):
        print(f"Welcome {a}")

s=Sample()
s.welcome("Deepak")


# __init__

class Sample:

    def __init__(self,name,city):
        self.name=name 
        self.city=city

    def display(self):
        print(f"Welcome {self.name} from {self.city} ")

s=Sample("Harish","Chennai")
s.display()


class Fruits:
    fruit1="Apple"
    fruit2="Banana"
    fruit3="Cherry"

    @classmethod
    def display(cls):
        print(f" {cls.fruit1} {cls.fruit2} {cls.fruit3} ")

f=Fruits()
f.display()


class Vehicles:
    @staticmethod
    def display(a):
        print(a)

v=Vehicles()
v.display("Coooopper")


# 1. Abstraction
# 2. Polymorphism
# 3. Encapsulation
# 4. inheritance

# inheritance:
# 1. Single inheritance
# 2. multilevel inheritance
# 3. multiple inheritance (Multiple Parents)
# 4. hierarchical inheritance (Multiple Child , 1 parent)

# 1. Single Inheritance

class Parent:
    def display_parent(self):
        print("I am from Parent")

class Child(Parent):
    def display_child(self):
        print("i am from Child")

c=Child()
c.display_child()
c.display_parent()


# 2.MultiLevel 

class Parent:
    def display_parent(self):
        print("I am from Parent")

class Child(Parent):
    def display_child(self):
        print("i am from Child")

class Grandchild(Child):
    def display_gchild(self):
        print("This is from GRandChild")

c=Grandchild()
c.display_parent()
c.display_child()
c.display_gchild()


# 3.Multiple Inheritance
class Parent1:
    def display_parent1(self):
        print("Parent 1")

class Parent2:
    def display_parent2(self):
        print("Parent 2")

class Child(Parent1,Parent2):
    def display_child(self):
        print("Child")

c=Child()
c.display_parent1()
c.display_parent2()
c.display_child()

# 1. Task:
class Flyer:
    def fly(self):
        print("I can Fly")

class Swim:
    def swm(self):
        print("I can Swim")

class Walk:
    def wlk(self):
        print("I can Walk")

class Duck(Flyer,Swim,Walk):
    pass
d=Duck()
d.fly()
d.wlk()
d.swm()

# 4.Hierarchical Inheritance

class Vehicles:
    def display(self):
        print("i am vehicle")

class Car(Vehicles):
    pass

class Bike(Vehicles):
    pass

class Train(Vehicles):
    pass

c=Car()
c.display()
b=Bike()
b.display()


class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def display(self):
        print(f"Brand Name :{self.brand}")

class Car(Vehicle):
    def __init__(self, brand,color):
        super().__init__(brand)
        self.color=color

    def show(self):
        #super().display()
        print(f" Brand {self.brand} Color {self.color}")

c=Car("Maruthi","red")
c.show()
#c.display()


# 2. Encapsulation
# 3. polymorphism
# 4. Abstraction

# Encapsulation

# protected : _ 
# private : __

class Userprofile:
    def __init__(self,username,mobile,password):
        self.username=username
        self._mobile=mobile 
        self.__password=password

    def get_password(self):
        print(self.__password)


u=Userprofile("Deepak",867890675,"deepak@123")
print(u.username)
print(u._mobile)
u.get_password()
print(u._Userprofile__password) # Name mangling




# Polymorphism:
# 1. overloading
# 2. overriding


# 1. overloading

class Calculation:
    def add(self,a,b,c=0,d=None):
        if d :
            print(a+b+c+d)
        else:
            print(a,b,c,d)
    
c=Calculation()
c.add(1,2)
c.add(1,2,3)
c.add(1,2,3,4)


# 2. overriding
class Animals:
    def sound(self):
        print("Animal Sound")

class Cat(Animals):
    def sound(self):
        print("Mewowoo")

c=Cat()
c.sound()


# 4.Abstraction:

from abc import ABC,abstractmethod
class Greet(ABC):
    def display(self):
        print("HI")

    @abstractmethod
    def welcome(self):
        pass
        
class Test(Greet):
    def sample(self):
        print("Python")

    def welcome(self):
        print("welcome")
t=Test()
t.display()
t.welcome()
t.sample()


class Grandparent:
    def __init__(self):
        print("Grand Parent")

class Parent1(Grandparent):
    def __init__(self):
        super().__init__() 
        print("parent 1")

class Parent2(Grandparent):
    def __init__(self):
        super().__init__() 
        print("parent 2")

class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__() 
        print("child")

c=Child()
print(Child.mro())
print(Child.__mro__)