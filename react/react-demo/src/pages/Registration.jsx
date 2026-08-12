import { useState } from "react"
export default function Registration(){
   const [produt_data,setProductData] = useState({
        "product_name":'',
        "price":0,
        "description":'',
        "rating":0
    })
    function addProduct(e){
        
        setProductData({...produt_data,[e.target.name]:e.target.value})
        console.log(produt_data)
    }
    return(
        <>
            <form method="POST">
                <input type="text" 
                    name="product_name" 
                    id="product_name" 
                    placeholder="product_name"
                    value={produt_data.product_name}
                    onChange={addProduct}
                    />
                <input type="number" 
                    value={produt_data.price}
                    onChange={addProduct} 
                    name="price" 
                    id="price" 
                    placeholder="price" />
                <input type="text" 
                    value={produt_data.description}
                    onChange={addProduct} 
                    name="description" 
                    id="description" 
                    placeholder="Description"/>
                <input type="number" 
                    value={produt_data.rating}
                    onChange={addProduct} 
                    name="rating" 
                    id="rating" 
                    placeholder="Rating" />
                <button type="submit">Submit</button>
            </form>
        </>
    )
}