# Base image
FROM python:3.11-slim

# Install system deps
RUN apt-get update && apt-get install -y \
    curl git build-essential zstd&& \
    rm -rf /var/lib/apt/lists/*

# Install Ollama CLI
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set workdir
WORKDIR /app

# Copy code
COPY ./app ./app
COPY ./requirements.txt ./requirements.txt

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
