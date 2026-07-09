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


hoisting:
var a;
console.log(a);
var a=10;