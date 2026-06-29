import datetime as d
print(d.datetime.now())
import datetime 
print(datetime.datetime.now())
print(datetime.datetime.now().year)
curdate=datetime.datetime.now()
print(curdate)
print(curdate.year)
print(curdate.strftime("%d %m %p %D %y %Y")) 

import time 
start_time= time.time()
# print("Hi")
# print("Hi")
# print("Hi")
time.sleep(3)
end_time= time.time()
print(time.process_time())

print(f"Total Execution Time { start_time-end_time}")

import math
print(math.ceil(5.1))
print(math.ceil(5.6))
print(math.floor(5.1))
print(math.floor(5.6))
print(math.pow(2,3))

import module as m
m.add(3,5)
import module
module.add(2,5)
print(module.mul(2,3))

from module import mul
print(mul(5,9))

# 2.File Handling

# mode:
# read  = "r"
# write = "w"
# append = "a"

file=open("sanjeev.txt",'w')
file.write("Welcome to File Handling")
file.close()

file=open("sanjeev.txt",'a')
file.write("Python Training")
file.close()

file=open("sanjeev.txt",'a')
file.write("\nHappy Learning")
file.close()

with open("sanjeev.txt",'a') as f:
    f.write("\n welcome")


# type 1: read
# type 2: readline
# type 3: readlines

with open("sanjeev.txt",'r') as f:
    print(f.read())

with open("sanjeev.txt",'r') as f:
    print(f.readline())

with open("sanjeev.txt",'r') as f:
    print(f.readlines())
    print(f.tell())
    print(f.seek(1))
    print(f.read(7))
    print(f.tell())

# Exception Handling

print(5/0)

# 1. try
# 2. except 
# 3. Exception
# 4. else 
# 5. finally
# 6. raise

try:
    a=5/0
except ZeroDivisionError:
    print(" number cannot divide by zero")


try:
    a=5/0
except ValueError:
    print("Value Error")
else:
    print("There is no error in this Program")


try:
    a=5/0
except (ValueError,ZeroDivisionError):
    print("Value Error")
else:
    print("There is no error in this Program")

try:
    a=int("abe")
except TypeError:
    print("type Error")
except ValueError as e:
    print("Error : ",e)


try:
    a="hello"
    b=5
    print(a+b)
except TypeError:
    print("Cannot add different datatype")

try:
    a=int("abe")
except Exception as e:
    print(e)

# raise




# decorator
# without changing original code expand the functionality
# @


def outer(func):
    def wrapper():
        print("HI")
        func()
    return wrapper

@outer
def greet():
    print("Welcome to skillfort")

greet()


# regex
# 1.search
# 2.match
# 3.test

import re
number="9908709888"
pattern=(r"^[6-9]\d{9}$")
print("valid" if re.match(pattern, number) else "invalid")


