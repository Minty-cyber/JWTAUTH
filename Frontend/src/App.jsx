import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import { SignUp, LogIn, VerifyEmail, ForgotPass } from "./components"

function App() {
  const [count, setCount] = useState(0)

  return (
    <>

    <Router>
      <Routes>
        <Route path='/'
          element = {<SignUp/>}
        
        </Route>
      </Routes>
    </Router>
      
    </>
  )
}

export default App
