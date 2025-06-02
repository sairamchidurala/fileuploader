FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# Ensure entrypoint is executable
RUN chmod +x ./entrypoint.sh

# Collect static at runtime
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "fileuploader.wsgi:application", "--bind", "0.0.0.0:8000"]
