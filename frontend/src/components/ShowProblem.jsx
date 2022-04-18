import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

function ShowProblem() {
  
  const [problem,setProblem]= useState({})
  const {id}=useParams()

  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000/problem/${id}`).then(data=>{
      console.log(data)
      setProblem(data.data)
    })
  },[])

  return (
    <div className='showproblem'>
      <div className="info">
        <h3 className="title">{problem.title}</h3>
        <div className="description">
          <p>{problem.description}</p>
        </div>
        <h2 className="difficulty">{problem.difficulty}</h2>
        <div className="solution">
          <p>{problem.solution}</p>
        </div>
      </div>
      <div className="ide"></div>
    </div>
  )
}

export default ShowProblem