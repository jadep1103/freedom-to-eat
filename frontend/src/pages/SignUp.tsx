// src/pages/SignUp.tsx 
import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";

export default function Signup()
{
    const { signup } = useAuth();
    const [username,setUsername] = useState("")
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await signup(username,email,password);
    };

    return(
        <div>
            <h1>Créer un compte</h1>
            <form onSubmit={handleSubmit}>
                <input type="text"
                        placeholder="Username"
                        value = {username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                /> 
                <input type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required/>
                <input  type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e)=>setPassword(e.target.value)} 
                        required/>


            <button type="submit">Register</button>
            </form>

        </div>
    );
}