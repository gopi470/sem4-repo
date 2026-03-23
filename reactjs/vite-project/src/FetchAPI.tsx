import { useEffect, useState } from "react";

type User = {
    id: number
    name: string
    email: string
}

function FetchAPI() {

    const [users, setUsers] = useState<User[]>([]);
    

    useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/users")
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP Error: ${response.status}`);
                }
                return response.json(); 
            })
            .then(data => {
                setUsers(data);
            })
            .catch(error => console.log(error));
    }, []);

   

    return (
        <>

        <div>
            {users.map(user => (
               <div>ID : {user.id}  , 
                    Name : {user.name}  , 
                    Email : {user.email}</div>
            ))}
        </div>
            
        </>
    );
}

export default FetchAPI;