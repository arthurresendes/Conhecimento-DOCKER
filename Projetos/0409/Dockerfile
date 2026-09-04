FROM python:3.10

WORKDIR /app

RUN pip install --no-cache-dir fastapi  uvicorn

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]


