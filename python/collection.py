1. list []
2. tuple ()
3. set {}
4. dict {"key":"value"}


1.list
    1. denoted by []
    2. mutable 
    3. ordered
    4. allow duplicate
    
list()

a=[1,2,3,3,4,5,3]

print(a)

2. tuple:
    1. denoted by ()
    2. Imutable 
    3. ordered
    4. allow duplicate 
    
a=(1,2,3,4,4)
print(type(a))
a=(1,)
print(type(a))



3 set 
    1. denoted by {}
    2. mutable
    3. unordered
    4. not allow duplicate
    
a={1,2,3,3,4,5}
print(a)


a=[1,2,3,3,4,5,5]
print(list(set(a)))

4.dict
    1 {"key":"value"}
    2. mutable
    3. ordered
    4. key - unique ,value allow duplicate
    
    
#list 

a=[1,2,3]
print(a[0])
# 1. append
# 2. extend
# 3. insert
a.append([1,2])
# a.append(1,2) # cant append more than one value
# a.extend(5,4) # cant append more than one value
print(a)
a.extend([5,4])
a.insert(2,9)
print(a)

# REmove
b=[1,2,3,4]
b.pop(2)
print(b)

c=[1,2,3]
c.clear()
print(c)

a=[1,2,3,4]
b=a.copy()
c=a
c.append(9)
print(a,b,c)

print(id(a),id(b),id(c))


m=[1,2,3,4,3,5,3,2,3]
print(m.count(3))

print(m.index(3))

n=[1,2,3,4,3,5,3,2,3]
n.reverse()
print(n)

i=[2,4,1,6,3,77,3,44,99]
i.sort()
print(i)
i.sort(reverse=True)
print(i)


# tuple

a=(1,3,4,3,4,4,4)
print(a.count(3))
print(a.index(5))

#set
a={1,2,3,4,5,5,6}
print(a)

b={1,2,3}
c={1,4,5}
print(b.union(c))  # |
print(b|c)
print(b.intersection(c)) # &
print(b.difference(c)) # -
print(b.symmetric_difference(c)) # ^

#dict
a={"name":"apple"}
print(a)
a["type"]="fruit"
print(a)
a["color"]="orange"
print(a)
a["color"]="red"
print(a)
print(a["name"])
print(a.get("name"))
print(a.get("names"))
print(a["names"])


b={"username":"user","first_name":"test1","last_name":"last","age":25}
print(b)
print(b.keys())
print(b.values())
print(b.items())

for i in b.values():
    print(i)


