import React , {useState} from 'react'

const SignUp = () => {
  const [formdata, setFormData] = useState({
    email:"",
    first_name:"",
    last_name:"",
    password:"",
    password2:"",
  })

  const { email, first_name, last_name, password, password2 } = formdata;

  const handleOnChange = (e) => {
    setFormData({
      ...formdata, [e.target.name]:e.target.value
    })
    
  }

  const [error, setError] = useState("")

  const handleSubmit = (e) =>{
    e.preventDefault()
    if (!email || !first_name || !last_name || !password || !password2){
      setError("All fields are required")

    }else{
      console.log(formdata)
      
    }
  }   
  return (
    <div className='form-container'>
      <div className='wrapper'>
        <div>
          <h2>Create Account</h2>
          <p style={{color:"red"}}>{error ? error: ""}</p>
          <form onSubmit={handleSubmit}>
              <div className='form-group'>
                 <label htmlFor="">Email Address:</label>
                 <input type="text"
                  className='email-form'  
                  name="email" 
                  value={femail} 
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
               <input type="submit" value= "Submit" className='submitButton' />
          </form>
        </div>
      </div>
    </div>
  )
}

export default SignUp
