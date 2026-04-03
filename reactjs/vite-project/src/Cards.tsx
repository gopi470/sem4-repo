
type model ={
    title :String,
    desc:String
}

function Card(props :model){
    return(
        <>
        <div className=" h-[200px] w-[200px] border-2 border-yellow-500 border-solid float float-left">
            <p className="font-bold text-xl pb-2">{props.title}</p>
            <p className="">{props.desc}</p>

        </div>
        </>
    )
};



export default Card;