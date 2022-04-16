import React from 'react'
import {useState,useEffect} from 'react'
import axios from 'axios'

function AddProblem() {

  const [problem, setproblem] = useState({})

  const handleSubmit = (e)=>{
    e.preventDefault()
    console.log(problem);
    axios.post('http://127.0.0.1:8000/addproblem',problem).then((data)=>{
      console.log(data);

    })
  }
  const handleChange = (e) =>{
  
    setproblem({...problem,[e.target.name]:e.target.value})
  }

  useEffect(()=>{
    console.log(problem);
  },[problem])
 
  return (
    <div>
       <form className="formclass">
              <div>
                <label for="title"> Enter Problem Title </label>
                <input type="text" name='title' id='firstname' onChange={handleChange}/>
              </div>

              <div>
                <label for="description"> Enter Problem description </label>
                <textarea name="description" cols="30" rows="10" onChange={handleChange}></textarea>
              </div>

              <div>
                <label for="difficulty"> Problem Difficulty </label>

                <select name="difficulty" onChange={handleChange}>
                  <option selected disabled> </option>
                  <option value="easy"> easy </option>
                  <option value="medium"> medium </option>
                  <option value="Hard"> Hard </option>

                </select>
              </div>

              <div>
                <label for="solution"> Problem Solution </label>
                <textarea name="solution" cols="30" rows="10" onChange={handleChange}></textarea>
              </div>

              <div>
                <input type="submit" value="AddProblem"  onClick={handleSubmit}/>
              </div>

            </form>
    </div>
  )
}

export default AddProblem