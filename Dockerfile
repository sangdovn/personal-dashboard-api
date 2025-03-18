# Use Python 3.12-alpine as base image
FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Copy and install dependencies first for better caching
COPY ./src/requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Gunicorn
ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
