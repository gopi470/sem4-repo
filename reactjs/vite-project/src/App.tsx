import Hello from "./Hello.tsx"
import Cards from "./Cards.tsx"

type model ={
    title :String,
    desc:String
}

const arr:model[] =[
  {title:"Speed",desc:"To utilize individual parts of their applicaion"},
  {title:"Flexibility",desc:"React code is easier to maintain"},
  {title:"Performance",desc:"Core of the framework"}
]

function App() {
  

  return (
    <>
     <Hello />
     <br />
     <Cards title={arr[0].title} desc={arr[0].desc} />
     <Cards title={arr[1].title} desc={arr[1].desc} />
     <Cards title={arr[2].title} desc={arr[2].desc} />
    </>
  )
}

export default App
