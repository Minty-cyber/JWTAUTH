import React , {useState} from 'react'

const SignUp = () => {
  const [formdata, setFormData] = useState({
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2: "",



  })
  return (
    <div className='form-container'>
      <div className='wrapper'>
        <div>
          <h2>Create Account</h2>
          <form action="">
              <div className='form-group'>
                 <label htmlFor="">Email Address:</label>
                 <input type="text"
                  className='email-form'  
                  name="email" 
                  value={formdata.email}  
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">First Name</label>
                 <input type="text"
                  className='email-form'  
                  name="first_name" 
                  // value={email}  
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Last Name</label>
                 <input type="text"
                  className='email-form'  
                  name="last_name" 
                  // value={email}  
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Password</label>
                 <input type="password"
                  className='email-form'  
                  name="password" 
                  // value={email}  
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Confirm Password:</label>
                 <input type="text" 
                 className='p'  
                 name="password2" 
                //  value={password2} 
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
