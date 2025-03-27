# Use a minimal Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-dev

# Copy the application code
COPY . .

# Expose port and run FastAPI
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "api.classify:app", "--host", "0.0.0.0", "--port", "8000"]
