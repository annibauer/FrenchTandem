
# French Tandem

A small Django + React app for practicing French conversation using OpenAI.

## Local development

### 1) Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

The API runs on http://localhost:8000.

### 2) Frontend

```bash
cd frontend
npm install
npm start
```

The React app runs on http://localhost:3000 and proxies API requests to the Django backend on port 8000.

## Environment variables

Create a local backend/.env file from the example:

```bash
cp backend/.env.example backend/.env
```

Then set a valid OpenAI key and Django secret.

## Notes

- The frontend dev server uses a proxy instead of a web socket backend.
- Do not commit real secrets.
- For production, use environment variables instead of hardcoded config.
