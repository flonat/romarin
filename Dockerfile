# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Debugging step: list installed packages to verify otree installation
RUN pip list

# Debugging step: list files in the application directory
RUN ls -l /app

# Ensure the static files directory exists
RUN mkdir -p /app/_static

# Collect static files using Django's collectstatic command
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variable for admin password
ENV OTREE_ADMIN_PASSWORD=GarciaFaria73!

# Run the command to migrate the database and start the server
CMD ["sh", "-c", "python manage.py migrate --noinput && otree prodserver 8000"]
