function :
    reuseable block of code for specific task 

Syntax: 
// Definition/declaration part
function function_name(){
    // statement
}
// Calling
function_name()


function sample(){
    console.log("hi")
}
sample()

Types : 
1. normal Function
2. Anonymous Function
3. arrow Function 
4. callback function 
5. Higher order function 

// 1.Normal Function:

function greet(){
    console.log("Welcome to Javscript Function")
}
greet()

function add (a,b){
    console.log(a+b)
}
add(12,5)
let z=20,y=30;
add(z,y)

// 2. Anonymus Function:
const sample=function (){
    console.log("I am example for anonymus function")
}
sample()
console.log(typeof(sample))

const test=10
console.log(typeof(test))

// 3. arrow Function
Syntax : () => {}

const test = (a) => { console.log(a)}
test(15)

const test1 = a => console.log(a)
test1("Apple")

const mul = (a,b) =>{ return a*b }
console.log(mul(5,10))

//4. callback function 
console.log("Hello")
setTimeout(()=>{console.log("Hi i am from callback")},2000)

setTimeout(testfunction,2000)
function testfunction(){
    console.log("welcome")
}


// Nested Function

function outer(){
    console.log("Hiii WElcome to Function Concept")
    function inner(){
        console.log("Inner Function")
    }
    inner()
    console.log("Outer Function")
}
outer()

// 5.higher order()
function outer(){
    console.log("Hiii WElcome to Function Concept")
    return function inner(){
        console.log("Inner Function")
    }
    console.log("Outer Function")
}
const innr=outer()
console.log(typeof(innr))
innr()

a=[1,2,3,4]
console.log(typeof(a))
console.log(a.map((i)=>{return i*2}))
console.log(a.filter((i)=>{return i%2==0 }))
console.log(a.reduce((a,c)=>{return a+c })) 


// Closure: 
// --------
function outer(){
    let i=0
    function inner(){
        return(i++)
    }
    return inner;
}
const clsr=outer();
clsr()
console.log(clsr())
clsr()
console.log(clsr())


function test(){
    let a=0
    console.log(a)
    a++
    console.log(a)
}

test()
test()

