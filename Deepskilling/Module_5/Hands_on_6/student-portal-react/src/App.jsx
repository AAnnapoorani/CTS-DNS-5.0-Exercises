import { useState } from "react";

import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Header from "./components/Header";
import ProtectedRoute from "./components/ProtectedRoute";

import Home from "./pages/Home";
import Courses from "./pages/Courses";
import CourseDetails from "./pages/CourseDetails";
import Profile from "./pages/Profile";

function App() {
  const [isLoggedIn, setIsLoggedIn] =
    useState(false);

  return (
    <BrowserRouter>
      <Header siteName="Student Portal" />
      <main>
        < div style={{ marginBottom: "20px" }} >
          < button onClick={() => setIsLoggedIn(!isLoggedIn)} >
            {isLoggedIn ? "Logout" : "Login"}
          </button>
          <p> Status: {isLoggedIn ? " Logged In" : " Logged Out"} </p>
        </div>
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/courses" element={<Courses />}/>
          <Route path="/courses/:id" element={<CourseDetails />}/>
          <Route path="/profile" element={ 
            <ProtectedRoute isLoggedIn={isLoggedIn}> <Profile /> 
            </ProtectedRoute> 
          }/>
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;