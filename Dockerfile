FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ ./backend
COPY frontend/ ./frontend

CMD ["python", "backend/app.py"]

