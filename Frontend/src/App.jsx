import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import { SignUp, LogIn, VerifyEmail, ForgotPass } from "./components"

function App() {
  return (
    <>

    <Router>
      <Routes>
        <Route path='/' element = {<SignUp/>} />
        <Route path='/login' element = {<LogIn/>} />
        <Route path='/dashboard' element = {<SignUp/>} />
        <Route path='/otp/verify' element = {<VerifyEmail/>} />
        <Route path='/forgot_pass' element = {<ForgotPass/>} />


      </Routes>
    </Router>
      
    </>
  )
}

export default App
