Operators
1. Arithmetic operator (+,-,*,/,%, //,**)
2. Assignment Operator (= , +=, -=, *=, /=)
3. Comparison Operator (==, >=,<= !=,>,<)
4. logical Operator (and or not)
5. Bitwise Operator (& | ^ ~) Xor - (1 0 = 1) , ~ 2scompliment ( -(x + 1))
6. membership Operator ( in ,not in)
7. Identity Operator 


a=10
b=5
c=a+b
print(c)

# 1. Arithmetic Operator

print(5+10)
print(10-5)
print(10*5)
print(11/2)
print(11 // 2)
print(2**3)

# 2. Assigment Operator
a=10
a,b=10,20
print(a,b)

c=5
c+=10 # c=c+10
print(c)

c=10
c-=5
print(c)

#3. Comparison Operator
a=5
b=5
print(a==b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)

logical
----------
and

0 0 =>  false
1 0 =>  false
0 1 =>  false
1 1 =>  True 

or 

0 0 =>  false
1 0 =>  True
0 1 =>  True
1 1 =>  True 

not
true => false
false => true

a=10
b=5
c=1
print(a>b and a>c)  # (10>5) and (10>1) t and  t  => T
print(a>b and a<c)  # (10>5) and (10<1) T  and  F => F

print(10 and 0)


a=10
b=5
c=1
print(a>b or a>c)  # t T => True
print(a>b or a<b)  # t F=> True

a=15
print(not a<0)

# Task : a=50 b=10 c=75  find biggest number 

2- 10
-   5- 0
-   2- 1
-   1- 0

1010 

Bitwise:
-------
(&=> and , | or , ^ xor , ~ not)

a=5 #=> 0101
b=1 #=> 0001

# 0101
# 0001
# -----
# 0001  and


# 0101
# 0001
# -----
# 0101  or

# 0101
# 0001
# -----  xor
# 0100

print(a&b)
print(a|b)
print(a^b)
a=5
print(~a)
>> <<

a=5   # 0001      01
a=4 # 0001    00

print(a>>2)
a=5 #010100
a=4 # 010000
print(a<<2)

# Membership 

a=[1,2,3,4,5]

print(6 in a)
print( 6 not in a)

#identity 
a=10
b=10
print(a is b)

a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)


a=[1,2,3,4]
b=[1,2,3,4]
print(a is not b)









    

