FROM python:3
WORKDIR /app
COPY requirements.txt .
COPY wait-for-it.sh .
COPY app.py .
COPY api api
RUN pip install -r requirements.txt
