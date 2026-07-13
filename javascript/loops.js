Loops:
1. for Loops -Entry level loop
2. while loop - Entry Level Loop 
3. do while loop -Exit level loop 


for Loop : 
-----------

Syntax: 

// Type 1:
for(initialization;condition;increment/decrement){
    //Statement
}

for(let i=1;i<=5;i++){
    console.log(i)
}
for (let i=5;i>=1;i--){
    console.log(i)
}

a="flower"
for( i of a){
    console.log(i)
}

b=["apple","orange","Banana"]
for(i in b){
    console.log(i)
}

for(i of b) {
    console.log(i)
}


a=[1,2,3,4]
// type2

for (i in a){
    console.log(i)
}

a=[1,2,3,4]
for (i of a){
    console.log(i)
}

while :
Syntax:

initialization;
while(condition){
    //statement
    // increment/decrement
}

let i=5;
while(i>=0){
    console.log(i)
    i--
}

Syntax:

initialization
do{
    //increment/Decrement
}while(condition)

let i=5;
do{
    console.log(i)
    i--;
}while(i>=0)


Condition:
----------
if 
if else 
else if 
Nested if

if 
     check whether the condition is true: 

Syntax: 

if (condition){
    // if Block
}

let age=18;
if (age>=18){
    console.log(" age is greater than or equal to 18")
}

let age=2;
if (age>=18){
    console.log(" age is greater than or equal to 18")
}
else{
    console.log("U r under 18")
}

let n=-10
if(n>0){
    console.log("Positive")
}else if(n<0){
    console.log("Negative")
}else{
    console.log("0")
}

let a=100
let b=25
let c=55

if (a>b && a>c)
{
    console.log("A is Bigger")
}else if(b>c){
    console.log("B is Bigger")
}else{
    console.log("C is Bigger")
}

let total=95
if(total>=35){
    if(total>=90 && total<=100){
        console.log("S GRADE")
    }else{
        console.log("pass")
    }

}
else{
    console.log("Fail")
}



