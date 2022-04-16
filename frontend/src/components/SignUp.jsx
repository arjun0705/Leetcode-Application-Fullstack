import React from 'react'
import axios from 'axios'
import {useEffect,useState} from 'react'

function Signup() { 
  const [user, setUser] = useState({})

  const handleChange = (e) =>{
    if(e.target.name === "isAdmin"){
    setUser({...user,[e.target.name]:e.target.checked?1:0})
    }
    else{
    setUser({...user,[e.target.name]:e.target.value})
  }}
 
  const handleSubmit = ()=>{
    axios.post('http://127.0.0.1:8000/signup',user).then((data)=>{
      console.log(data);

    })
  }

  useEffect(()=>{
    axios.post('http://127.0.0.1:8000/signup',user).then(
      (data)=>{
        console.log(data);

      }
    )
  },[])

  useEffect(()=>{
    console.log(user);
  },[user])
 
  return (
          <div>
            <form action="" className="formclass">
              <div>
                <label for="firstname"> Enter Firstname </label>
                <input type="text" name='firstName' id='firstname' onChange={handleChange}/>
              </div>

              <div>
                <label for="lastname"> Enter Lastname </label>
                <input type="text" name='lastName' id='lastname' onChange={handleChange} />
              </div>

              <div>
                <label for="email"> Enter Email </label>
                <input type="text" name='email' id='email' onChange={handleChange}/>
              </div>

              <div>
                <label for="password"> Enter Password </label>
                <input type="text" name='password' id='password' onChange={handleChange} />
              </div>

              <div>
                <input type="checkbox" name='isAdmin' id='isAdmin' onChange={handleChange} />
                <label for="isAdmin"> Signup as Admin  </label>
              </div>

              <div>
                <input type="submit"  onClick={handleSubmit}/>
              </div>

            </form>
          </div>
  )
}

export default Signup