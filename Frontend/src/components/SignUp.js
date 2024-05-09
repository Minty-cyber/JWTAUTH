import React , {useState} from 'react'

const SignUp = () => {
  return (
    <div>
      <div>
        <div>
          <h2>Create Account</h2>
          <form action="">
              <div className='form-group'>
                 <label htmlFor="">Email Address:</label>
                 <input type="text"
                  className='email-form'  
                  name="email" 
                  value={email}  
                  />
               </div>
               <div className='form-group'>
                 <label htmlFor="">Email Address:</label>
                 <input type="text"
                  className='email-form'  
                  name="email" 
                  value={email}  
                  />
               </div>c
          </form>
        </div>
      </div>
    </div>
  )
}

export default SignUp
