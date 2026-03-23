
import { useState } from "react";
import { useEffect } from "react";






function Counter(){

    const [text,setText]=useState(0)



     useEffect(()=>{
        document.title=` ${text}`
    })

    function increment(){
        setText(text+1)
    }

     function decrement(){
        setText(text-1)
    }

    return(
        <>
        <br />
        <p>{text}</p>
        <button className="border-solid border-[2px]" onClick={increment}>Increment</button>
        <br />
        <button className="border-solid border-[2px]" onClick={decrement}>Decrement</button>
        </>
    )
}


export default Counter;