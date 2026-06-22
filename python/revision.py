names_list = ["Arun","mm","laya"]
ages_list = [14,23,22]
grades_list = ["9th","r4","e3"] 

var=list(zip(names_list, ages_list, grades_list))

for i,m,n in var:
    print(i)
    print(m)
    print(n)
    
for i in var:
    for j in i:
        print(j)


for name, age, grade in zip(names_list, ages_list, grades_list):
    print(name,age,grade)
    
    