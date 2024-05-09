import React, {useState} from 'react'


const VerifyEmail = () => {
    
  return (
    <div>
        <div className='form-container'>
            <form action="" style={{width:"30%"}}>
               <div className='form-group'>
                 <label htmlFor="">Enter your Otp code:</label>
                 <input type="text"
                  className='email-form'  
                  name="otp"
                //   value={otp}
                //   onChange={(e)=>setOtp(e.target.value)} 
                   />
               </div>
               <button type='submit' className='vbtn'>Send</button>
            </form>
        </div>
    </div>
  )
}

export default VerifyEmail