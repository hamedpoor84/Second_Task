# Use an official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first
COPY requirements.txt .

# Update pip
RUN pip install --upgrade pip

# Install aiohttp separately
RUN pip install aiohttp

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]