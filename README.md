# FastAPI Bug Tracker

This is a **FastAPI-based bug tracking system** using **SQLAlchemy, Alembic, and PostgreSQL**.

## 🚀 Installation Guide

### 1️⃣ Install **Pyenv** and **Python 3.11.11**

Make sure you have **Pyenv** installed:

```sh
curl https://pyenv.run | bash
```

```sh

pyenv install 3.11.11
pyenv virtualenv 3.11.11 bugtrackerenv
pyenv activate bugtrackerenv
```

- U had venv for project

# 📦 Install Project Dependencies

Install requirements from the file:

```sh
pip install -r requirements.txt
```

# ⚙️ Environment Configuration

Create a .env file in your project root:

```sh
DATABASE_URL=postgresql+psycopg2://your_user:your_password@localhost:5432/your_db_name
SECRET_KEY=your_secret_key_here
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
```

Replace with your actual PostgreSQL connection details.

# 🛠 Alembic Database Migrations

Initialize Alembic (only once):

```sh
alembic init migrations
```

Set the correct DB URL in alembic.ini or env.py.

Generate and apply migrations:

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

# 🧪 Run the App

```sh
fastapi dev main.py
```

# 📚 API Documentation

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc
