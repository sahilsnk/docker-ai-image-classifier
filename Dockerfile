# Use an official lightweight Python image
FROM python:3.10-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Ensure Gunicorn is installed and accessible
RUN pip install gunicorn

# Expose port 5000 for Flask
EXPOSE 5000

# Start the application using Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
