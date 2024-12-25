import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { LoginForm } from '../components/LoginForm';
import './Login.css';

const Login = () =>{

  return (
    <div className="container">
      <LoginForm/>
      </div>


  );
};

export default Login;
