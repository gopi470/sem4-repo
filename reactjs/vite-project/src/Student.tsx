

type t1={
    rollNo:number
    name: String
    department: String
}

function Student(props:t1){
    return(
        <>
        <br />
        <div>RollNo :{props.rollNo} , Name :{props.name} , Department : {props.department}</div>
        </>
    )
}


export default Student;