FROM python:3
WORKDIR /app
COPY requirements.txt app.py ./
COPY api api
RUN pip install --upgrade pip && \
    pip install -r requirements.txt