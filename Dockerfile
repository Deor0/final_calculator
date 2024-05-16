# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system packages for Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Set the display environment variable for Tkinter
ENV DISPLAY=:0

# Run the application
CMD ["python", "app.py"]
