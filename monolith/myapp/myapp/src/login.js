// Import the react JS packages 
import axios from "axios";
import {useState} from "react";
// Define the Login function.
export const Login = () => {
     const [username, setUsername] = useState('');
     const [password, setPassword] = useState('');
     // Create the submit method.
     const submit = async e => {
          e.preventDefault();
          const user = {
                username: username,
                password: password
               };
          // Create the POST requuest
          const {data} = await                                                                            
                         axios.post('http://localhost:8000/token/',
                         user ,{headers: 
                        {'Content-Type': 'application/json'},
                         withCredentials: true});
         
         localStorage.clear();
         localStorage.setItem('access_token', data.access);
         localStorage.setItem('refresh_token', data.refresh);
         axios.defaults.headers.common['Authorization'] = 
                                         `Bearer ${data['access']}`;
         window.location.href = '/'
    }
    return(
      <>
<div className="row">
<div className="offset-3 col-6">
    <h1>Log In</h1>
    <form onSubmit={submit} id="create-presentation-form">
      <div className="form-floating mb-3">
        <input
         onChange={e => setUsername(e.target.value)}
          value={username}
          placeholder="name"
          required
          type="text"
          id="name"
          className="form-control"
        />
        <label htmlFor="presenter_name">Username</label>
      </div>
      <div className="form-floating mb-3">
        <input
          type="text"
          onChange={e => setPassword(e.target.value)}
          value={password}
          placeholder="Picture"
          id="text"
          className="form-control"
        />
        <label htmlFor="presenter_name">Password</label>
      </div>

      <button className="upload">Submit</button>
    </form>
  </div>
</div>
</>
     )
}