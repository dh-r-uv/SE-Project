# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# (Optional) This line would install dependencies if requirements.txt had any
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application when the container starts
CMD ["python", "calculator.py"]