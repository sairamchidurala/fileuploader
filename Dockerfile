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

# Provide a default ALLOWED_HOSTS for build time (adjust as needed)
ENV ALLOWED_HOSTS=localhost

# Run migrations and collectstatic during image build
RUN python manage.py migrate --noinput && python manage.py collectstatic --noinput

# Expose port (optional but good practice)
EXPOSE 8000

# Start the server directly as CMD
CMD ["gunicorn", "fileuploader.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
