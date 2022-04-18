import axios from 'axios'
import React from 'react'
import{useState} from 'react' 

function Login() {
  
  const [user, setuser] = useState({})

  const handleChange = (e) =>{
    setuser({...user,[e.target.name]:e.target.value})
  }

  const handleSubmit = (e)=>{
    e.preventDefault()
    axios.post('http://127.0.0.1:8000/login',user).then((data)=>{
      console.log(data);

    })
  }

  return (
    <div className='login'>
        <form>
        <div><h1>Login Form</h1></div>
             <div>
                <label for="email"> Enter Email </label>
                <input type="text" name='email' id='email' onChange={handleChange}/>
              </div>

              <div>
                <label for="password"> Enter Password </label>
                <input type="text" name='password' id='password' onChange={handleChange} />
              </div>

              <div>
                <input type="submit"  onClick={handleSubmit}/>
              </div>
        </form>        

    </div>     
  )
}

export default Login