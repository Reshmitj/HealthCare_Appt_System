import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { Link } from 'react-router-dom';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    role: 'patient'
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const csrfToken = Cookies.get('csrftoken');

    try {
      await axios.post(
        'http://localhost:8000/api/accounts/register/',
        formData,
        {
          withCredentials: true,
          headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
          }
        }
      );
      setMessage('✅ Registration successful!');
      setFormData({ username: '', email: '', password: '', role: 'patient' });
    } catch (err) {
      console.error(err);
      setMessage('❌ Registration failed. Please try again.');
    }
  };

  return (
    <div className="container-center">
        <div className="topnav">
  <span className="brand">Healthcare App</span>
</div>

      <form className="form-box" onSubmit={handleSubmit}>
        <h2>Register</h2>
        {message && <p className="message">{message}</p>}

        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <select name="role" value={formData.role} onChange={handleChange}>
          <option value="patient">Patient</option>
          <option value="doctor">Doctor</option>
        </select>

        <button type="submit">Register</button>

        <p style={{ marginTop: '10px' }}>
          Already have an account? <Link to="/login">Login here</Link>
        </p>
      </form>
    </div>
  );
}

export default Register;
