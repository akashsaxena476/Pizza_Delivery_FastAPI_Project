# Pizza_Delivery_FastAPI_Project

A backend Pizza Delivery API built using FastAPI, implementing JWT-based authentication, user management, and order processing. The project uses SQLAlchemy ORM for database operations and follows RESTful API design principles, making it suitable for real-world scalable applications.


** Features :**

- User Signup & Login (JWT Authentication)

- User Management

- Order Placement & Tracking

- Update & Delete Orders

- Role-Based Access (User / Superuser)

- Order Status Management


**Tech Stack :**

Backend: FastAPI

Database: PostgreSQL / SQLite

ORM: SQLAlchemy

Authentication: fastapi-jwt-auth

Server: Uvicorn

Backend : FastAPI

Database : PostgreSQL

ORM : SQLAlchemy

Authentication : fastapi-jwt-auth

Server : Uvicorn


**How to run the Project**

- Install Postgreql
- Install Python
- Git clone the project with  git clone https://github.com/jod35/Pizza-Delivery-API.git
- Create your virtual environment
- Install the requirements with pip install -r requirements.txt
- Set Up your PostgreSQL database and set its URI in your database.py
- engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>', echo=True)
- Create your database by running python init_db.py
- Finally run the API ``` uvicorn main:app ``
