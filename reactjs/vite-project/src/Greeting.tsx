

type t1={
    name:String
}

function Greeting(props:t1){
    return(
        <>
        <br />
        <div>Hello {props.name}</div>
        </>
    )
}


export default Greeting;