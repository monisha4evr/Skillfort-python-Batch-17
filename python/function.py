function
    - reusable block of code- to perfsorm some specific action 

syntax: 

function definition /declaration
def function_name():
    # statement



function Calling
function_name()


print("Example for Function")
def add():
    print(5+10)
print("Example for Function ends here....")

add()


types:
    1.buit-in (print() etc...)
    2.user defined
    3.lambda funciton
    4.recursion 

# user defined:

1. arguments - actual value  on function calling  
2. parameters - on function definition

# types:
# 1. without argument without return
# 2. without argument with return
# 3. with argument without return
# 4. with argument with return


def add():
    print(5+10)

add()

def greet():
    print("Welcome  to Python  Function")

greet()

print(greet)

# Type 2: 
# without argument with return

# example 1
def greet():
    return ("Welcome")

gt=greet()
print(gt)

#example 2:
def greet():
    txt="Welcome"
    return txt

sample=greet()
print(sample)

#example 3:

def greet():
    txt="Welcome to function"
    return txt

print(greet())

#type 3:
#with argument without return

def add(a,b): # parameters
    print(a+b)

add(5,10)  # argument

#example 2:

def add(a,b,c):
    print(a+b+c)

x=10
y=20
z=30
add(x,y,z)
add(1,2,3)
add(1,5,8)

#4. with argument with return

def mul(a,b,c):
    return a*b*c

print(mul(3,5,9))
result=mul(5,10,2)
print(result)


#arguments type:
# 1. positional argument
# 2. keyword argument
# 3. named argument
# 4. arbitary arguments


#1. positional arguments
#example 1

def add(a,b,c):
    print(a,b,c)

add(1,2,3)

def sample(a,b,c):
    print(a,b,c)

sample(c=1,b=2,a=3)

# example for error
def sample(a,b,c):
    print(a,b,c)

sample(b=1,a=2,1) #SyntaxError: positional argument follows keyword argument
sample(5,b=2,a=3) # TypeError: sample() got multiple values for argument 'a'

def sample(a,b,c,/):
    print(a,b,c)

sample(1,c=4,b=2)  #error     ~~~~~~^^^^^^^^^^^TypeError: sample() got some positional-only arguments passed as keyword arguments: 'b, c'

def sample(a,/,b,c):
    print(a,b,c)

sample(1,c=4,b=2) #1 2 4


def sample(a,b,*,c):
    print(a,b,c)

sample(1,c=4,b=2)

# error program starts
def sample(a,b,*,c):
    print(a,b,c)

sample(1,c=4,2) # error program

def sample(a,b,/,*,c):
    print(a,b,c)

sample(1,c=4,b=2) # error program

# error program ends

#type 3 Named Argument

def user_profile(a,b="user"):
    print(a,b)

user_profile("deepak","deepak_123")
user_profile("naveen")

#type 4 arbitary *, ** args,kwargs

def sample(a,*b):
    print(a)
    print(b)

sample(1,2,3,4,5,6,7,8)

def funcname(a,**b):
    print(b)

a=10
funcname(a,name="apple",color="red",price="105")

Task 1: count Vowels
task 2: FActorial
task 3: palindrome
task 4: count even number in list [3,4,5,6,7,2,9,1]
task 5: sum of List Element



# lambda function:
# -----------------
# Singleline Expression
# Anonymous Function
# Syntax: lambda p1,p2 : expression 

sample = lambda a,b,c : a+b+c
print(sample(10,20,30))

map()
filter()
reduce()

a=[1,2,9,3,4,5,6]
res=map(lambda i:i*2,a)
print(list(res))

result =filter(lambda i:i%2==0,a)
print(list(result))

from functools import reduce
r=reduce(lambda b,c : b+c,a)
print(r)

# Generator:
# ---------

def fname():
    yield 1
    yield 2
    yield 3
    
f=fname()
print(next(f))
print(next(f))
print(next(f))

my_list=['pytohn','java','react']
a=iter(my_list)

while True:
    try:
        print(next(a))
    except StopIteration:
        break











