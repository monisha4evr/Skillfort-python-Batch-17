a="apple"
# print(type(a))
print(a[-4])
# a=0 -5
# p=1 -4
# p=2 -3
# l=3 -2
# e=4 -1

# 1.slicing
# --------
#Syntax: [start,end,step]

a="python"
# p 0
# y 1
# t 2
# h 3
# o 4
# n 5

print(a[1:4])
print(a[0:6:2])
print(a[::-1])
print(a[3:])
print(a[:4])
print("REVERESE",a[3:0:-2])

a="apple" + " is a Fruit" 
print(a)

a="apple "+ 5
print(a)

a="apple"*3
print(a)
a="apple" *0
print("Example",a)

a="welcome To Python"

print(len(a))
print(a.count('e'))
print(a.find('z'))
print(a.index('z'))
print(a.capitalize())
print(a.upper())
print(a.strip())
print(a.endswith('n'))






