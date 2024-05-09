import React from 'react'

const LogIn = () => {
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
             
             <input type="submit" value= "Submit" className='submitButton' />
        </form>
      </div>
    </div>
  </div>
  )
}

export default LogIn