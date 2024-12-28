FROM python:3.12-slim

WORKDIR /app

COPY main.py /app

RUN mkdir -p /app/test_data

CMD ["python", "main.py"]