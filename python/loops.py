loops
1. for 
2. while 

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
initialization

while condition :
    # statement
    increment/decrement
    
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
    
 
Task
--------   
*****
*****
*****
*****
*****

1
12
123
1234
12345

1
22
333
4444
55555

    
    
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*" *i)

*****
****
***
**
*

     *
    **
   ***
  ****
 *****
 



    

    

    




