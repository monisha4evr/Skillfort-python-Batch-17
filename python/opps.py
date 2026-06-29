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
        print(f" Brand {self.brand} Color {self.color}")

c=Car("Maruthi","red")
c.show()