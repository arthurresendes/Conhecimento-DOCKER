FROM python:3

RUN apt-get update -y && \
    apt-get install -y default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install flask requests flask_mysqldb

EXPOSE 5000

CMD ["python", "./app.py"]
