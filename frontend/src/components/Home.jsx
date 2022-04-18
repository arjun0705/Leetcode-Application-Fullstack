import axios from 'axios'
import React, { useEffect, useState } from 'react'

function Home() {
  const [original,setOriginal] = useState([])
  const [data,setData] = useState([])

  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/problems').then(data=>{
      console.log(data)
      setOriginal(data.data.data)
      setData(data.data.data)
    })
  },[])

  return (
    <div className='home'>
      <div>
        <input type="text" placeholder='Search' />
      </div>
      <table>
        <tr>
        <th>S.no</th>
        <th>Title</th>
        <th>Description</th>
        <th>Difficulty</th>
        <th>Solution</th>
        <th>View</th>
        <th>Delete</th>
        </tr>
        {
        data.map((e,i)=>(
          <tr key={i+1}>
            <td>{i+1}</td>
            <td>{e.title}</td>
            <td>{e.description}</td>
            <td>{e.difficulty}</td>
            <td>{e.solution}</td>
            <td>view</td>
            <td>delete</td>
          </tr>

        ))
      }
      </table>
    </div>
  )
}

export default Home