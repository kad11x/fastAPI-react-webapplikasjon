import React, { useState } from "react";
import axios from "axios"; // Use Axios to send data to FastAPI
import './ContactForm.css';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    userName: "",
    user_Password: "",
    user_Fierstname: "",
    user_Lastname: "",
    user_Email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);

    try {
      const response = await axios.post("http://localhost:8000/api/user/", formData);
      alert("Form submitted successfully!");
      window.location.href = "/";
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
            name="userName"
            value={formData.userName}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
          <h4>Password</h4>
          <input
            type="password"
            name="user_Password"
            value={formData.user_Password}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
          <h4>First Name</h4>
          <input
            type="text"
            name="user_Fierstname"
            value={formData.user_Fierstname}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
          <h4>Last Name</h4>
          <input
            type="text"
            name="user_Lastname"
            value={formData.user_Lastname}
            onChange={handleChange}
            required
          />
        </div>

        <div className="register-input-box">
          <h4>Email Address</h4>
          <input
            type="email"
            name="user_Email"
            value={formData.user_Email}
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
