/*alert("Example for External Script")*/

a=10;
console.log(`Hello world ${a}`)
Variable:
a="helloworld"
console.log(a)
console.log(a)
console.log(a)
console.log(a)
console.log(a)

Scope:
1. public Scope
2. Functional Scope
3. Block Scope

let a=10;
console.log(a)
function fname(){
    console.log(a)
}

let functional/Block scope
const -functional/block scope
var  - Public Scope

var :
1. Public Scope 
2. allow -redeclare
3. allow reassign 
4. no need initialization 
5. support hoisting

let :
1. Functional/Block Scope 
2. not allow - redeclare
3. allow reasssign
4. no need initialization
5. support but put in TDZ

const :
1. Functionsl/Block Scope 
2. not allow - redeclare
3. not allow reasssign
4. Need initialization at Declaration time
5. support but put in TDZ

Temporal Dead Zone.

const a=10;
console.log("Outer",a);
function fname(){
    console.log("Inside Function",a);
    if(1){
        console.log("Inside Block",a)
    }
}
fname();
console.log("Outer function",a);


function test(){
    let a=10;
    console.log("inside Function",a)
    if(1){
        console.log("Inside the Block",a)
    }

}
test()
console.log("outside the Funciton",a)

function sample(){
    for(let i=1;i<=5;i++){
        console.log("Inside",i)
    }
    console.log("Outside",i)
}
sample()

Operator:
----------
1. Arithmetic(+,-,*,/,%,++,--)
    pre increment/post increment

    a=5
    a++ // POST: 5 - 6 - assign then Increment
   a=5=> ++a // PRE : 6 increment - asign

   a=5
   console.log(++a)
   console.log(a)

   b=5
   b++
   ++b
   console.log(b++)
   console.log(b)


   c=15
   c++
   console.log(++c)
   console.log(++c)
   console.log(c++)
   ++c
    console.log(c)

2. Assignment (+=,=,-=,*=,/=)
3. Comparision(==,>=,<=,>,<,===,!===,!=)
    console.log('5'==5)
    console.log(5==5)
    console.log(5===5)
    console.log('5'===5)

4. Logical (&& || !)

console.log(5+4+"3")
console.log("3"+5+4)

console.log(null == undefined)
console.log(null === undefined)

console.log([]==[])
