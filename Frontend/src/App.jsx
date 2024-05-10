import { useState } from 'react'

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

import SignUp from './components/SignUp';
import LogIn from './components/LogIn';
import VerifyEmail from './components/VerifyEmail';

function App() {
  return (
    <>

    <Router>
      <Routes>
        <Route path='/' element = {<SignUp/>} />
        <Route path='/login' element = {<LogIn/>} />
        <Route path='/dashboard' element = {<SignUp/>} />
        <Route path='/otp/verify' element = {<VerifyEmail/>} />
       


      </Routes>
    </Router>
      
    </>
  )
}

export default App
