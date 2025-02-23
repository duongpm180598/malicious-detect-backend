# Use a Python base image
FROM python:3.10.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (if you have one)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port your Flask app listens on (default is 5000)
EXPOSE 5000

# Set the environment variable for Flask (if needed)
# For production, consider using a WSGI server like Gunicorn
ENV FLASK_APP=app.py 
# ENV FLASK_ENV=development # Only for development. Remove or set to production for production.

# Command to run when the container starts
# For development:
CMD ["flask", "run", "--host=0.0.0.0"] # Allows access from outside the container
# For production (using Gunicorn):
# CMD ["gunicorn", "--bind=0.0.0.0:5000", "your_app_name:app"] # Replace your_app_name:app