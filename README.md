# 🍽️ Food Menu Tracker API (Keploy Assignment 3)

A simple **Flask-based REST API** to manage a restaurant's menu. Built as part of **Keploy’s Backend Testing Bootcamp** to demonstrate API development, unit testing, integration testing, and API testing using Postman.

---

## 📚 Table of Contents
1. [About the Project](#about-the-project)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Installation](#installation)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [Screenshots](#screenshots)
8. [How to Run](#how-to-run)
9. [Author](#author)

---

## 📌 About the Project

This project allows you to:
- Add, update, delete, and retrieve food items in a restaurant menu.
- Perform CRUD operations using RESTful endpoints.
- Run **unit tests** for individual functions.
- Run **integration tests** to validate the full API behavior.
- Test API using **Postman**.
- Achieve good **test coverage** and follow best practices.

---

## 💻 Tech Stack

- 🐍 Python 3.11
- 🔥 Flask
- ✅ Unittest (for testing)
- 🌐 Postman (for API testing)
- 📋 Keploy (for API test generation – optional)

---

## 🚀 Features

- `POST /menu` → Add a new item  
- `GET /menu` → Retrieve all menu items  
- `PUT /menu/<name>` → Update an item by name  
- `DELETE /menu/<name>` → Delete an item by name  
- Unit testing and Integration testing using `unittest`
- Manual API testing via Postman

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/food-menu-api
cd food-menu-api
pip install flask
🧪 Testing
✅ Unit Tests
Located in tests/test_app.py

Tests core logic functions like add_item()

🔄 Integration Tests
Located in tests/test_integration.py

Checks full API flow with Flask test client

🌐 API Tests via Postman
Manual testing done using Postman

Endpoints tested:

POST /menu

GET /menu

PUT /menu/<name>

DELETE /menu/<name>

🧑‍💻 How to Run Locally
bash
Copy
Edit
python app.py
Then open: http://127.0.0.1:5000/menu in your browser or Postman.

To run tests:

bash
Copy
Edit
cd tests
python test_app.py
python test_integration.py

✍️ Author
Thiraviya (Thiya)
📌 AI & Data Science Student
🔗 LinkedIn
💻 Passionate about APIs, Python, AI and Real-Time Applications
