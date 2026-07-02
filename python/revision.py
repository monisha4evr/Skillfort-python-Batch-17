a=[1,2,3]
b=[1,2,3,5]
c=b
d=b.copy()
d.append(7)
c.append(6)
print(id(a),id(b),id(c),id(d))
print(b)


a=10
b=10
print(id(a),id(b))


a=(1,2,3)
print(type(a))
p=list(a)
print(type(p))



a=10
b=20
a,b=b,a
print(a,b)


a=[1,2,3] + 5
print(a)


a="flower"
print(a[1:3])
print(a[::-1])


a=4 


def add(a,**b):
    print(b)

add(2,b=2,c=3,d=4,e=5)



class Agelimit(Exception):
    pass

def checkage(age):
    if age<18:
        raise Agelimit(" AGe is Lesser")
   
try:
   checkage(16)
except Agelimit as e:
    print(e)
        


a=[1,2,3]
b=[1,2,3]
c=b
d=b.copy()
c.append(4)
d.append(5)
print(b,d)


a="flower"
print(a[1:3])

def test(a,**b):
    print(b)
test(1,b=2,c=3,d=5,f=6)

a= "I like Flowers"

a=['i',"am","Learning","python"]
print(' '.join(b))

print("ABC"[1]) #B