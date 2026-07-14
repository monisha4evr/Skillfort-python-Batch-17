
fetch('url')
.then() // convert json to oject
.then() // use object

javascript object Notation

fetch('https://fakestoreapi.com/products/1')
            .then(res=>res.json())            
            .then(json=>console.log(json))