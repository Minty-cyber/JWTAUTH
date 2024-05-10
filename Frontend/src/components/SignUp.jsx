import React , {useState} from 'react'
import axios from 'axios'
import {useNavigate} from "react-router-dom"
import {toast } from 'reac'

const SignUp = () => {
  const redirect = useNavigate();
  const [formdata, setFormData] = useState({
    email:"",
    first_name:"",
    last_name:"",
    password:"",
    password2:"",
  })

  const { email, first_name, last_name, password, password2 } = formdata; //Destructuring very important
  const [loading, setLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");


  const handleOnChange = (e) => {
    setFormData({
      ...formdata, [e.target.name]:e.target.value
    })
    
  }

  const [error, setError] = useState("")

  const handleSubmit = async (e) =>{
    e.preventDefault();
    if (!email || !first_name || !last_name || !password || !password2){
      setError("All fields are required");

      setTimeout(() => {
        setError("")
      }, 2000);
       //the error message disappears after some time
    }else{
      const res = await axios.post('http://localhost:8000/api/auth/register', formdata)// Add formdata to the backend 

      if (res.status == 200) {
        redirect("/otp/verify")

      }
      // setLoading(true) //starting the loading when the form is submitted
      // setTimeout(() => {
      //   setLoading(false); //Removing the loading from there
      //   setSuccessMessage("Account Created Successfully") 
      //   setTimeout(() => {
      //     setSuccessMessage("") 
      //   }, 2000);//Initializing the message
      // },2000)
      
      
    }
  }   
  return (
    <div className='form-container'>
      <div className='wrapper'>
        <div>
          <h2>Create Account</h2>
          <p style={{color:"red"}}>{error}</p>
          <p style={{color:"green"}}>{successMessage}</p>
          <form onSubmit={handleSubmit}>
              <div className='form-group'>
                 <label htmlFor="">Email Address:</label>
                 <input type="text"
                  className='email-form'  
                  name="email" 
                  value={email} 
                  onChange={handleOnChange} 
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">First Name</label>
                 <input type="text"
                  className='email-form'  
                  name="first_name" 
                  value={first_name}  
                  onChange={handleOnChange} 

                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Last Name</label>
                 <input type="text"
                  className='email-form'  
                  name="last_name" 
                  value={last_name}  
                  onChange={handleOnChange} 

                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Password</label>
                 <input type="password"
                  className='email-form'  
                  name="password" 
                  value={formdata.password}  
                  onChange={handleOnChange} 

                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Confirm Password:</label>
                 <input type="text" 
                 className='email-form'  
                 name="password2" 
                 value={password2} 
                 onChange={handleOnChange} 
                 />
               </div>
               <button type="submit" className='submitButton' disabled={loading}>
              {loading ? 'Loading...' : 'Submit'}
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default SignUp
