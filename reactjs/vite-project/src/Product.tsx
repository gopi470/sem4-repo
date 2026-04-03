

type t1={
    name:String
    price:number
    inStock:boolean
}

function Products(props:t1){
    return(
        <>
        <br />
        <div>Name :{props.name}  Stock:{props.inStock ===true ? "Available" : "NotAvailable"}</div>
        </>
    )
}


export default Products;