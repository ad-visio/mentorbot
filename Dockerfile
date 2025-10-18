FROM python:3.11-slim
WORKDIR /app
COPY placeholder.py /app/placeholder.py
CMD ["python", "/app/placeholder.py"]
