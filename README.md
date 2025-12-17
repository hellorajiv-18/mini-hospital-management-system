# Mini Hospital Management System (HMS)

This is a Mini Hospital Management System built as part of an internship assignment.  
The system focuses on **doctor availability management** and **patient appointment booking** with proper **role-based access control** and **race-condition safety**.

---

## 🚀 Features

### 👨‍⚕️ Doctor
- Doctor can log in securely
- Doctor can add availability time slots (date & time)
- Doctor can view only their own availability slots
- Booked slots are clearly marked and blocked

### 🧑‍💼 Patient
- Patient can log in securely
- Patient can view all available (unbooked) doctor slots
- Patient can book an available slot
- Once booked, the slot becomes unavailable to others

---

## 🔐 Authentication & Authorization
- Session-based authentication using Django
- Custom User model with roles: **DOCTOR** and **PATIENT**
- Role-based access using custom decorators
- Unauthorized access returns **403 Forbidden**

---

## 🧠 Race Condition Handling (Important)
To prevent multiple patients from booking the same slot at the same time:
- Database transactions are used
- Row-level locking is implemented using:
  - `transaction.atomic()`
  - `select_for_update()`

This ensures **only one patient can book a slot**, even under concurrent requests.

---

## 🛠️ Tech Stack

- **Backend:** Django
- **ORM:** Django ORM
- **Authentication:** Django session-based auth
- **Database:** SQLite (for local demo; PostgreSQL planned)
- **Frontend:** Django Templates (HTML)

---

## ▶️ How to Run Locally

### 1. Clone the repository
### 2. Create and activate virtual environment
### 3. Install dependencies
### 4. Run migrations
### 5. Create superuser
### 6. Run server

## Author

**Rajiv Sharma**  
BCA Student | Aspiring Backend Developer


