
data type: 
---------

Number
number - 10  - int
decimal - 15.3 - float


None
boolean - True/False  - bool

sequence
string - "Apple" - str
list 
tuple  immutable
set

dict {k=>v} 

a= {1,2,3,4,5}


mutable - can change
immutable - can't change

ordered - 
unordered - 


type()

a=10
print(type(a))

b=10.3
print(type(b))


c="Flower"
print(type(c))


id()

a=10
b=10

print(id(a),id(b))

a=[1,2,3,4]
b=[1,2,3,4,5]

print(id(a),id(b))


a="apple"
b="apple"
print(id(a),id(b))


type conversion:

1.implicit ( Automatic)
2.explicit ( manual )

a=10
b=10.5
c=a+b
print(type(a))
print(type(b))
print(type(c))

a=int("123")
b=45
print(a+b)

#Task :
a=input("Enter a value")
a=int(input("enter a value"))

a="123"
print(int(a)) #123

a="-123"
print(int(a)) # -123
a="+123"
print(int(a)) # 123

a="123a"
print(int(a)) #ValueError: invalid literal for int() with base 10: '123a'

a="abc"
print(int(a)) #ValueError: invalid literal for int() with base 10: 'abc'

b="1.2"
print(float(b)) #1.2
b="-1.2"
print(float(b)) #-1.2
b="+1.2"
print(float(b)) #1.2
b="1"
print(float(b)) #1.0

# float to int
a=1.2
print(int(a)) #1

a=1
print(float(a)) #1.0

a='123'
print(bool(a)) #True
a=''
print(bool(a)) #False

