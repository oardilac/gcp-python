FROM python:3.9-buster

ENV PYTHONUNBUFFERED True

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy only specific directories and files
COPY app /app/app
COPY gcp /app/gcp
COPY manage.py /app/

# Create static files directory
RUN mkdir -p /app/staticfiles

# Run Django-specific commands
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Start server
CMD exec gunicorn gcp.wsgi:application --bind 0.0.0.0:$PORT
