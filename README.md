Installation steps:
1. Pull the repository
2. Navigate to the root directory
3. Create a virtual environment (python -m venv env)
4. Activate the environment (source env/bin/activate)
5. Install the dependencies (pip install -r requirements.txt)
6. Create .env file, copy the contents from .env.example)
7. Run the migrations: (alembic upgrade head)
8. Start the app: (python src/app.py)