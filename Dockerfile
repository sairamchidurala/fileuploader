FROM python:3.9-slim as builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

# Expose port (optional but good practice)
EXPOSE 8000

# Start the server and run migrations/collectstatic at container startup
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn fileuploader.wsgi:application --bind 0.0.0.0:8000 --workers 4"]
