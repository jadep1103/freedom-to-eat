// src/context/AuthContext.tsx
import { createContext, useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

type User = {
  id: string;
  username: string;
  email: string;
};

type AuthContextType = {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  signup: (username: string, email: string, password: string) => Promise<void>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const navigate = useNavigate();

  // Fonction pour récupérer les infos user depuis /auth/me avec token
  const fetchUser = async (token: string) => {
    const res = await fetch("http://localhost:8000/auth/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!res.ok) {
      throw new Error("Impossible de récupérer l'utilisateur");
    }
    const userData: User = await res.json();
    setUser(userData);
  };

  // Au montage, on check si token en localstorage, on récupère l'user
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      fetchUser(token).catch(() => {
        // token invalide ou autre, on déconnecte
        logout();
      });
    }
  }, []);

  const login = async (email: string, password: string) => {
    const response = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error("Échec de la connexion");
    }

    const data = await response.json();
    const token = data.access_token;

    localStorage.setItem("token", token);

    await fetchUser(token);

    navigate("/food");
  };

  const signup = async (username: string, email: string, password: string) => {
    const response = await fetch("http://127.0.0.1:8000/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, email, password }),
    });

    if (!response.ok) {
      throw new Error("Échec de l'inscription");
    }

    // Si tu veux auto-login après signup, tu peux appeler login ici :
    await login(email, password);

    // Sinon tu peux juste faire : navigate("/login");
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    navigate("/login");
  };

  return (
    <AuthContext.Provider value={{ user, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
};
