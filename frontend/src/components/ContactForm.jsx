import React, { useState } from "react";
import axios from "axios"; // Use Axios to send data to FastAPI
import './ContactForm.css';
//import { FaUser,FaLock } from "react-icons/fa";

const ContactForm = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    firstName: "",
    lastName: "",
    email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);

    try {
      const response = await axios.post("http://localhost:8000/api/user", formData);
      alert("Form submitted successfully!");
      console.log("Server Response:", response.data);
    } catch (error) {
      console.error("Error submitting form:", error);
      alert("Failed to submit form. Please try again.");
    }
  };

  return (
    <div className="register-wrapper">
      <form onSubmit={handleSubmit}>
        <h2>Register User</h2>
        <h3>Personal Information</h3>

        <div className="register-input-box">
        <h4>Username</h4>
          <input
            type="text"
            name="username"
            placeholder=""
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
        <h4>Password</h4>
          <input
            type="password"
            name="password"
            placeholder=""
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
        <h4>First Name</h4>
          <input
            type="text"
            name="firstName"
            placeholder=""
            value={formData.firstName}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
        <h4>Last Name</h4>
          <input
            type="text"
            name="lastName"
            placeholder=""
            value={formData.lastName}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
        <h4>Email address</h4>
          <input
            type="email"
            name="email"
            placeholder=""
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ContactForm;