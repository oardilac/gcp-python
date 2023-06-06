FROM python:3.9-buster

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Start server
CMD ["gunicorn", "gcp.wsgi:application", "--bind", "0.0.0.0:8000"]