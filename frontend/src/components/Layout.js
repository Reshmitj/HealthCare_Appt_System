import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Layout.css';

function Layout({ children, role }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.clear(); // ✅ Clear username and role
    navigate('/login');
  };
  

  return (
    <div className="layout">
      <div className="sidebar">
        <h3>Menu</h3>
        <nav>
          <Link to={role === 'doctor' ? '/dashboard/doctor' : '/dashboard/patient'}>🏠 Dashboard</Link>

          {role === 'patient' && (
            <>
              <Link to="/book-appointment">📅 Book Appointment</Link>
              <Link to="/appointments/my">📖 View My Appointments</Link>
            </>
          )}

          {role === 'doctor' && (
            <Link to="/doctor-appointments">📋 View Appointments</Link>
          )}
        </nav>
      </div>

      <div className="main">
        <header className="topbar">
          <div className="brand">Healthcare App</div>
          <button onClick={handleLogout} className="logout-btn">Logout</button>
        </header>
        <div className="content">{children}</div>
      </div>
    </div>
  );
}

export default Layout;
