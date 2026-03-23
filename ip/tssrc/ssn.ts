
console.log("hello");

const arr :string[] =["🌟 Specialized Centre of Excellence in Prosthetics and Orthotics “SAJAY-CEPO” established♛","🏆 SSN students win 1st place in Smart India Hackathon 2025","♛ S. Rohit Krishna (3rd Year) becomes India’s 89th Grandmaster in Chess"]

const id =document.getElementById("news");

if(id) {id.textContent="News"}
let index:number=0;

const func=()=>{
    if( id && arr[index]){
         id.textContent=arr[index] ?? ""; 
         index = (index + 1) % arr.length
    } 

}

func();

const timerid=setInterval(func,5000);