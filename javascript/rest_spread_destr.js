1. Rest // Pack rest of the Element
2. Spread  // Unpack
3. Destructuring  // Rest

// Rest (Parameter)  and Spread( array )
//... as spread operator

const fruits=['apple','orange','banana']
const fruits1=['grapes',"Cherry"]
console.log(fruits,fruits1)

const frts1=[fruits,fruits1] 
console.log(frts1) // [ [ 'apple', 'orange', 'banana' ], [ 'grapes', 'Cherry' ] ]
const frts=[...fruits,...fruits1]
console.log(frts) // [ 'apple', 'orange', 'banana', 'grapes', 'Cherry' ]

//... as rest operator
// In function declaration

function add(a,b,...c){
    console.log(a,b,c)
}

add(1,2,3,4,5)


//Destructuring
// 1. Array Destructuring
// 2. Object Destructuring
// unpack 
// 1. Array Destructuring
const fruits = ['apple','orange','cherry']
const[z,a]=fruits;
console.log(z)

// 2. Object Destructuring
const person_details = {firstname:"harish",lastname:"M",address:"Chennai"}
const {firstname:fn,lastname,address}=person_details;
console.log(fn)