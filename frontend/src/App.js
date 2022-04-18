import './App.css';
import {Link, Route, Routes} from 'react-router-dom'
import Home from './components/Home';
import AddProblem from './components/AddProblem';
import DeleteProblem from './components/DeleteProblem';
import UpdateProblem from './components/UpdateProblem';
import Signup from './components/SignUp';
import Login from './components/Login';
import ShowProblem from './components/ShowProblem';

function App() {
  return (
    <>
    <div className="nav">
    <span> LOGO </span>
    <ul>
      <Link to="/"><li>Home</li></Link>
      <Link to="signup"><li>Signup</li></Link>
      <Link to="Login"><li>Login</li></Link>
      <Link to="addproblem"><li>AddProblem</li></Link>
    </ul>
  </div>

  <Routes>
    <Route path='/' element={<Home/>} />
    <Route path='addproblem' element={<AddProblem/>} />
    <Route path='showproblems/:id' element={<ShowProblem />} />
    <Route path='updateproblem/:id' element={<UpdateProblem/>} />
    <Route path='deleteproblem' element={<DeleteProblem/>} />
    <Route path='signup' element={<Signup/>} />
    <Route path='login' element={<Login/>} />


  </Routes>
   </>
  );
}

export default App;
