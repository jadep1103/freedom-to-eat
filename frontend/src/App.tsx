import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from './pages/LandingPage.tsx'; 
import Login from './pages/Login.tsx';
import SignUp from './pages/SignUp.tsx';
import Home from './pages/Home.tsx'; 

function App() {

return (

  <Router>
    <Routes>
      <Route path="/" element={<LandingPage/>}></Route> 
      <Route path="/login" element={<Login/>}></Route> 
      <Route path="signup" element={<SignUp/>}></Route>
      <Route path="home" element={<Home/>}></Route>
    </Routes>
  </Router>

);

}

export default App;