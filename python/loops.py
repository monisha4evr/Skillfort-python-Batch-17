# loops
# 1. for 
# 2. while 

#range(start,end,step)

print(list(range(1,6)))

for i in range(1,6):
    print(i)
    
for i in range(0,11,2):
    print(i)
    
a=[1,2,3,4,5]
for i in a:
    print(i*5)
    
    
fruits=["apple","orange","Banana","Cherry"]
for i in fruits:
    print(i)
    
name="flower"
rev=''
for n in name:
     rev=n+rev
print(rev)

# n=f  rev=f
# n=l  rev=l+f => lf
# n=o  rev= o+lf => olf

a=[1,2,3,4]
tot=0
for i in a:
    tot+=i
print(tot)

#syntax:
# initialization

# while condition :
#     # statement
#     increment/decrement
    
i=1
while i<=5:
    print(i)
    i=i+1
    
    
i=5
while i>=1:
    print(i)
    i=i-1
    
a=123
rev=0
while a>0 :
    remind=a%10
    rev=rev*10+remind
    a//=10
    
print(rev)

for i in range(1,6):
    print(i)
 

#Execution
# a=123
# a>0 123>0 T    
#     remind=a%10  123%10 => 3
#     rev=0*10+3 => 3
#     a=12
# 12>0 True
#     12%10(2)
#     rev=3*10(30)+2 => 32
#     a//=10 12//10 =1
    
# 1>0 True
#     1%10 (1)
#     rev=32*10 +1 321
#     a//=10
    
 
# Task
# --------   
# *****
# *****
# *****
# *****
# *****

# 1
# 12
# 123
# 1234
# 12345

# 1
# 22
# 333
# 4444
# 55555
    
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*" *i)

# *****
# ****
# ***
# **
# *

#      *
#     **
#    ***
#   ****
#  *****

 

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

for i in range(11):
    print(i)
    
a=[1,2,9,4,5]
for i in a:
    print(i)


# ----------------------

for i in range (1,6):
    print("*"*i)
    
for i in range (1,7): 
    for j in range(1,i):
        print(j,end="")
    print()
 
# execution     


# i=1 
#     range(1) => j=0         => *  
#              => j=1(F)
             
# i=2
#     range(2) 
#         => j=0             =>**
#         => j=1
        
# i=3
#     range(3)
#         =>j=0
#         =>j=1
#         =>j=2        =>***
        
        
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
    
    
# 1
# 22
# 333
# 4444
# 55555


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    
rows=5   
for i in range(1,rows):
    print(" "*(rows-i)  + "*"* i )
    
    
a=[1,2,2,3,4,4,5,6]
#print(list(set(a)))
uniquevalue=[]
for i in a:
    if i not in uniquevalue:
        uniquevalue.append(i)
        
print(uniquevalue)

# break
# continue
# pass


age=21
if age>20:
    pass

def fname():
    pass

print("Loops Start Here")
for i in range(11):
    print(i)
    if i==5:
        break

print("Loops Ends here")


print("Loops Start Here")
for i in range(11):
   
    if i==5:
        continue
    print(i)
print("Loops Ends here")

# enumerate
# zip
# List and Dictionaries comprehension

for i,n in enumerate(range(1,11)):
    print(i,n)

a=["name","username","password"]
b=["Ganesh","ganesh_1510","ganesh@123","address"]

for i,v in zip(a,b):
    print(i,v)

print([i**i for i in range(11)])
print([i for i in range(11) if i%2==0])


a=["name","username","password"]
b=["Ganesh","ganesh_1510","ganesh@123"]
print({i:v for i,v in zip(a,b)})


Task 1:

5*1=5
5*2=10

Task 2:
"even" 1 even 3 even 5

task 3:

Flower



for i in range(11):
    print("even" if i%2==0 else i)

#    ( or )

print([i if i%2==1 else "Even" for i in range(11)])

a="flower"
vowels=['a','e','i','o','u']
cnt=0
consonent=0
for i in a:
    if i in vowels:
        cnt+=1
    else:
        consonent+=1
print(cnt)
print(consonent)

# Task 4:
# --------
[10,20,15,20,30,40] # remove Function

# task 5:
# --------

[1,9,5,3,7,4,2] #sort

# task 6:  

[0,4,3,0,1,0,6]
output:[1,3,4,6,0,0,0]

a= [0,4,3,0,1,0,6]
for i in range(len(a)):
    for j in range(i):
        if a[i] != 0 :
            a[i],a[j]=a[j],a[i]
print(a)

   












    




