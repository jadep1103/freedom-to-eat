// src/context/AuthContext.tsx 
//pas de backend relié so far
import { createContext, useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

type User = 
{
    id: string;
    username: string;
    email: string;
};

type AuthContextType = 
{
    user: User | null;
    login: (email: string, password: string) => Promise<void>;
    signup: (username: string, email: string, password: string) => Promise<void>;
    logout: () => void; 
}; 

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);
    const navigate = useNavigate();
  
    
      // On appelle le backend ici 
      const login = async (email: string, password: string) => {
        // On appelle le backend ici 
        const response = await fetch("http://localhost:8000/login"), {
          method: "POST",
          headers: {
              "Content-Type":"application/json",
          }, 
          body: JSON.stringify({email,password}),
        };
      if (!response.ok)
      {
        throw new Error("Échec de la connexion")
      }

      const data = await response.json();
      const token = data.access_tokern;

      // Stocker le token dans le local storage 
      localStorage.setItem("token",token);

      navigate("/food");

      };
    
  
    
  
    return (
      <AuthContext.Provider value={{ user, login, signup, logout }}>
        {children}
      </AuthContext.Provider>
    );

    const signup = async (username: string, email: string, password: string) => {
        const response = await fetch("http://localhost:8000/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, email, password }),
        });
    
        if (!response.ok) {
          throw new Error("Échec de l'inscription");
        }
    
        const data = await response.json();
        const token = data.access_token;
    
        localStorage.setItem("token", token);
        navigate("/journal");
      };
    
      const logout = () => {
        localStorage.removeItem("token");
        navigate("/login");
      };
    
  
  export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) throw new Error("useAuth must be used within AuthProvider");
    return context;
  };