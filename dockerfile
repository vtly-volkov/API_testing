# Use the official Python image as the base image
FROM python:3.12-slim

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the project files
COPY . /app
WORKDIR /app

# Run pytest with allure reporting
CMD ["pytest"]
