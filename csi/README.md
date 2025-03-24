# Django Project Setup Guide

This guide provides instructions on setting up an **existing** Django project, including installing dependencies, configuring settings, and running the server.

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- Virtual environment (venv)

## Step 1: Clone the Repository
```sh
git clone https://github.com/Araar-Taha/CSI_backend.git
cd csi
```

## Step 2: Create and Activate a Virtual Environment
A virtual environment keeps project dependencies isolated.

### Windows (Command Prompt)
```sh
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)
```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

## Step 4: Configure Environment Variables
If the project uses environment variables, create a `.env` file in the root directory and add the required settings (refer to `.env.example` if available).

## Step 5: Apply Migrations
```sh
python manage.py migrate
```

## Step 6: Create a Superuser (For Admin Panel)(Optional)
```sh
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

## Step 7: Run the Development Server
```sh
python manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check if the project is running.

## Additional Commands
### Collect Static Files (For Deployment)
```sh
python manage.py collectstatic
```

### Run Tests
```sh
python manage.py test
```

## Step 8: Freeze Requirements (If Updating Dependencies)
```sh
pip freeze > requirements.txt
```


