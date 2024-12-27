import React, { useState } from 'react';
import './LoginForm.css';
import { FaUser, FaLock } from "react-icons/fa";
import axios from 'axios';

export const LoginForm = () => {
  const [userName, setUsername] = useState('');
  const [user_Password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Send POST request to the API endpoint
      const response = await axios.post('http://localhost:8000/api/user/login/', {
        userName,
        user_Password,
      });

      if (response.status === 200) {
        setSuccessMessage('Login successful!');
        setErrorMessage('');
        // Optionally redirect or perform other actions on success
        console.log('Logged in successfully', response.data);
        window.location.href = "/Home";
      }
    } catch (error) {
      // Handle error cases
      if (error.response && error.response.status === 401) {
        setErrorMessage('Invalid username or password.');
      } else {
        setErrorMessage('An error occurred. Please try again.');
      }
      setSuccessMessage('');
    }
  };

  return (
    <div className="wrapper">
      <form onSubmit={handleLogin}>
        <h1>Login</h1>

        {errorMessage && <p className="error-message">{errorMessage}</p>}
        {successMessage && <p className="success-message">{successMessage}</p>}

        <div className="input-box">
          <input
            type="text"
            placeholder="Username"
            value={userName}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <FaUser className="icon" />
        </div>
        <div className="input-box">
          <input
            type="password"
            placeholder="Password"
            value={user_Password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <FaLock className="icon" />
        </div>

        <div className="remember-forgot">
          <label>
            <input type="checkbox" /> Remember me
          </label>
          <a href="#">Forgot password?</a>
        </div>

        <button type="submit">Login</button>

        <div className="register-link">
          <p>
            Don't have an account? <a href="/register">Register</a>
          </p>
        </div>
      </form>
    </div>
  );
};
