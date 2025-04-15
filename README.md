# 🚀 Healthcare Appointment System - Setup Guide

This is a Full Stack Healthcare Appointment System built using **React** (Frontend) and **Django** (Backend) with **SQLite** database.

---

## 🛠️ Prerequisites

Ensure you have the following installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.x](https://www.python.org/)
- [Node.js & npm](https://nodejs.org/)

---

## 🚀 Running the Backend (Django)

1. Open a terminal in VS Code:

```bash
cd backend
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the Django development server:

```bash
python manage.py runserver
```

> Backend will be running at: `http://localhost:8000`

---

## 💻 Running the Frontend (React)

1. Open a **new terminal tab** or window in VS Code:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

> Frontend will be available at: `http://localhost:3000`

---

## ❓ Troubleshooting

- **CSRF or CORS Errors**  
  Ensure the backend server is running and CSRF cookies are correctly being sent from the backend.

- **Dependency Errors**  
  Try running:

```bash
npm install
```

---

## ✅ You're all set!

Visit the app in your browser at `http://localhost:3000` and log in or register to start using the system.

---

## 📁 Folder Structure Overview

```plaintext
HealthCare_Appt_System/
│
├── backend/              # Django Backend
│   ├── accounts/         # User, Profile, Appointments app
│   ├── db.sqlite3        # SQLite database
│   └── manage.py         # Django management script
│
└── frontend/             # React Frontend
    ├── public/
    └── src/
```

## 👤 Default Login Credentials (for Testing)

| **Role**       | **Username**   | **Password**         |
|----------------|----------------|----------------------|
| Doctor         | `Jones`        | `test`               |
| Patient        | `patient1`     | `test`               |
| Receptionist   | `reception1`   | `securepass123`      |

> You can register new users through the registration form or pre-load them into the database for demos.
