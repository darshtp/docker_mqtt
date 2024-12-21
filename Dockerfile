# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to the container
COPY mqtt_sub.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port (optional, not needed since it's a subscriber)
EXPOSE 1883

# Command to run the application
CMD ["python", "mqtt_sub.py"]
