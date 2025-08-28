# 🏥 E-Hospitality Management System

The **E-Hospitality Management System** is a Django-based web application designed to manage hospital operations such as **patient registration, doctor registration, appointment booking, billing/invoice generation, and health resources management**.  
This project uses **SQLite** as the database backend.

---

## 🚀 Features

### 👩‍⚕️ Doctor Module
- Doctor registration and login
- Profile management
- View patient appointments
- Manage availability

### 🧑‍🤝‍🧑 Patient Module
- Patient registration and login
- Update patient details
- Book appointments with doctors
- View medical history and invoices

### 💳 Payment & Billing
- Generate invoices for patient appointments
- Store and display billing history
- Secure payment integration (basic flow with SQLite)

### 🔐 Authentication
- Separate login/registration for patients and doctors
- Secure password storage with Django authentication system
- Forgot password/reset functionality

### 📑 Admin Module
- Manage doctors and patients
- View and delete records
- Access complete hospital reports

---

## 🛠️ Tech Stack

- **Backend:** Django 4.2 (Python 3.13)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django DB)
- **Version Control:** Git & GitHub

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/e_hospitality.git
   cd e_hospitality
