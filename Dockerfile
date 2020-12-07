FROM python:3
WORKDIR /app
COPY requirements.txt .
COPY app.py .
COPY api api
RUN pip install -r requirements.txt