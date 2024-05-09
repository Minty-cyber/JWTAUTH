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
        <Route path='/' element = {<SignUp/>} />
        <Route path='/login' element = {<LogIn/>} />
        <Route path='/dashboard' element = {<SignUp/>} />
        <Route path='/otp/verify' element = {<VerifyEmail/>} />
        <Route path='/' element = {<ForgotPass/>} />


      </Routes>
    </Router>
      
    </>
  )
}

export default App