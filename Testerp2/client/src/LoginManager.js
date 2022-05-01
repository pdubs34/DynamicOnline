import React from "react";
import LoginAccessor from "./Accessor/LoginAccessor"
import { Link } from "react-router-dom";
import "./App.css"


export default class LoginManager extends React.Component{
    state = {
      username: '',
      password: '',
      receivedData: ''
    };
    // componentDidMount() {
    //   this.setState({
    //     username: this.user1.getUsername(),
    //     password: this.user1.getPassword(),
    //     },
    //   );
    // }
   
    handleUsernameChange = (event) => {
      this.setState({username: event.target.value});
    }
    handlePasswordChange = (event) => {
      this.setState({password: event.target.value});
    }
    
    handleSubmit = (event) => {
      event.preventDefault();
      const { username, password } = this.state;
      this.tempUser = new LoginAccessor(username, password);
      this.tempUser.validateLogin(username,password);
    }
   
    render() {
      return (
        <>
         <form onSubmit={this.handleSubmit}>
          <h2>Username</h2>
          <input name="username" className="form-control" id="username" placeholder="Enter username" value={this.state.username} onChange={this.handleUsernameChange} />
          <h2>Password</h2>
          <input name="password" className="form-control" id="password" placeholder="Enter password" value={this.state.password} onChange={this.handlePasswordChange} />
          <br></br>
          <button type="submit" className="btn btn-success btn-block">Submit</button>
          </form>
          <div className="LoginManager">
          <Link to="/NewLogin">Forgot Password?</Link> 
          </div>
        </>
      );
    }
  } 