import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Layout from '../components/Layout';
import '../styles/main.css'; 
import Cookies from 'js-cookie';


function BookAppointment() {
  const [doctors, setDoctors] = useState([]);
  const [formData, setFormData] = useState({
    doctor: '',
    date: '',
    time: ''
  });
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/accounts/doctors/', { withCredentials: true })
      .then(res => setDoctors(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const csrfToken = Cookies.get('csrftoken'); // ✅ Get CSRF token
  
    try {
      await axios.post(
        'http://localhost:8000/api/accounts/appointments/book/',
        formData,
        {
          withCredentials: true,
          headers: {
            'X-CSRFToken': csrfToken  // ✅ Set CSRF token in header
          }
        }
      );
      setMessage('✅ Appointment booked successfully!');
      setFormData({ doctor: '', date: '', time: '' });
    } catch (err) {
      console.error(err);
      setMessage('❌ Failed to book appointment. Try again.');
    }
  };
  

  return (
    <Layout role="patient">
      <div className="form-box" style={{ maxWidth: '500px', margin: 'auto' }}>
        <h2>Book Appointment</h2>
        {message && <p className="message">{message}</p>}

        <form onSubmit={handleSubmit}>
          <label>Select Doctor</label>
          <select
            name="doctor"
            value={formData.doctor}
            onChange={handleChange}
            required
            className="input-field"
          >
            <option value="">-- Choose --</option>
            {doctors.map(doc => (
              <option key={doc.id} value={doc.id}>{doc.username}</option>
            ))}
          </select>

          <label>Date</label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
            className="input-field"
          />

          <label>Time</label>
          <input
            type="time"
            name="time"
            value={formData.time}
            onChange={handleChange}
            required
            className="input-field"
          />

          <button type="submit" className="btn-primary">Submit</button>
        </form>
      </div>
    </Layout>
  );
}

export default BookAppointment;
