# socialmedia_app
This is a social media app that allows users to create posts, like and comment on posts, and follow other users. And users can chat with eachother as well. The app uses the Django framework and the Django REST framework for the backend. The frontend is built using Vite and Vanilla JS.

## Features
- Create posts
- Like and comment on posts
- Follow other users
- Chat with other users

## System requirements
- Python 3.8+

## Getting Started
1. Clone the repository
```bash
git clone https://github.com/nidhi-tagline/socialmedia-app.git
```

2. Navigate to the project directory
```bash
cd socialmedia-app
```

3. Create a virtual environment and activate it.
```bash
python -m venv env
source env/bin/activate
```

4. Create .env file by copying .env.example and add your environment variables.
```bash
cp .env.example .env
```

5. Install the requirements.
```bash
pip install -r requirements.txt
```

6. Makemigrations and migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Run the development server
```bash
python manage.py runserver
```

8. Open http://127.0.0.1:8000/ in your browser
